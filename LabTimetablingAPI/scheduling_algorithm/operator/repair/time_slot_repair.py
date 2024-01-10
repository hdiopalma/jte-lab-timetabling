import random
from math import floor
from datetime import timedelta

from scheduling_algorithm.structure import Chromosome, TimeSlot
from scheduling_algorithm.data_parser import ModuleData, GroupData, Constant

from scheduling_algorithm.operator.repair.base_repair import BaseRepair

class TimeSlotRepair(BaseRepair):
    def __init__(self):
        super().__init__("RepairTimeSlot")
        self.module_data = ModuleData
        self.group_data = GroupData
    
    def __call__(self, chromosome: Chromosome):
        """
        Repairs the time slots in the given chromosome by checking the availability of time slots for each gene.
        If a time slot is not available, it finds a feasible solution within the start and end dates of the module's schedule.
        If no feasible solution is found, it try to randomly generate a time slot, if it is somehow not available, then it will return the original time slot.

        Args:
            chromosome (Chromosome): The chromosome to be repaired.

        Returns:
            Chromosome: The repaired chromosome.
        """
        # chromosome = deepcopy(chromosome)
        for index, gene in enumerate(chromosome):
            start_date = self.module_data.get_dates(gene['module']).start_date
            end_date = self.module_data.get_dates(gene['module']).end_date
            schedule = self.group_data.get_schedule(gene['group'])
            if not self.check_available_time_slot(gene['time_slot'], schedule):
                time_slot = self.find_feasible_solution(start_date, end_date, schedule)
                if time_slot is None:
                    time_slot = gene['time_slot']
                chromosome.set_time_slot(index, time_slot)
        return chromosome
    
    def check_available_time_slot(self,time_slot: TimeSlot, schedule=None):
        if schedule:
            return schedule[time_slot.day][time_slot.shift]
        return False
    
    def find_feasible_solution(self, start_date, end_date, schedule, max_iteration=100):
        """Find a feasible solution for the gene by randomly generating a time slot until it is available"""
        for _ in range(max_iteration):
            time_slot = self.choose_available_time_slot(start_date, end_date, schedule)
            if self.check_available_time_slot(time_slot, schedule):
                return time_slot
        return None
    
    def choose_available_time_slot(self,start_date, end_date, schedule):
        """Choose a random available time slot for the gene"""
        if start_date.weekday() != 0:
            start_date = start_date + timedelta(days=7 - start_date.weekday())
        week_duration = (end_date - start_date).days + 1
        available_time_slots = [TimeSlot(start_date, day, shift) for day, shifts in schedule.items() for shift, available in shifts.items() if available]
        #if there is no available time slot, then return a random time slot
        if len(available_time_slots) == 0:
            return self.generate_time_slot(start_date, end_date)
        
        random_time_slot = random.choice(available_time_slots)
        random_week = random.randint(0, week_duration)
        #calculate the date
        random_date = start_date + timedelta(days=random_week * 7 + Constant.days.index(random_time_slot.day))
        return TimeSlot(random_date, random_time_slot.day, random_time_slot.shift)
    
    def generate_time_slot(self, start_date, end_date):
        """Generate time slots based on the start date, end date, days and shifts"""
        #if start_date not start from Monday, then start from the next Monday
        if start_date.weekday() != 0:
            start_date = start_date + timedelta(days=7 - start_date.weekday())
        duration = (end_date - start_date).days + 1
        weeks_duration = floor(duration / 7)
        random_weeks = random.randint(0, weeks_duration)
        random_days = random.choice(Constant.days)
        random_shifts = random.choice(Constant.shifts)
        random_date = start_date + timedelta(days=random_weeks * 7 + Constant.days.index(random_days))
        return TimeSlot(random_date, random_days, random_shifts)