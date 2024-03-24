# jte-lab-timetabling

**Phase 1: Project Setup and Planning**

1. **Project Kickoff:**
   - Review your project requirements, goals, and constraints. ✅
   - Set clear objectives for scheduling system. ✅

2. **Problem Analysis:**
   - Understand the scheduling problem thoroughly. ✅
   - Identify all the constraints, preferences, and data sources. ✅

3. **Project Planning:**
   - Break down project into manageable tasks. ✅
   - Create a timeline or Gantt chart to allocate time for each task. ✅

4. **Data Collection and Preparation:**
   - Gather data about participants, assistants, modules, laboratories, and existing schedules. ✅

**Phase 2: Algorithm Development**

5. **Algorithm Design:**
   - Design hybrid meta-heuristics algorithm (Genetic Algorithm + Tabu Search). udah ehe ☑️ (entah bener atau engga, masih bisa dikembangin)
   - Define the fitness function that evaluates schedule quality. ☑️ (Masih bisa dikembangin atau ditambahin lagi)

6. **Algorithm Implementation:**
   - Create a separate module or package for scheduling algorithm. ✅
   - Implement the Genetic Algorithm and Tabu Search components. ✅
   - Implement genetic operators (crossover, mutation) and neighborhood moves for Tabu Search. ✅

**Phase 3: API Development**

7. **Django Project Setup:**
   - Create a new Django project. ✅ (Sebenernya udah lama kelar ya ini? soalnya desain algoritmanya langsung didalem django)
 
8. **Create Apps:**
   - Create separate apps for different aspects of your project:
     - `scheduling_api` for general system functionality. ✅
     - `scheduling_algorithm` for the scheduling algorithm. ✅
     - `scheduling_algorithm_api` for scheduling algorithm-related API. ✅ udah? soalnya foldernya diapus, sekarang nyatu ama `scheduling_algorithm`

9. **Define API Endpoints:**
   - In `scheduling_api/urls.py`, define endpoints for submitting data and retrieving schedules. ✅ (eh folder ini juga diapus sih, sekarang tiap API diurus di tiap app masing2 aja, ngga terlalu ribet juga lagian (ribet sih))
   - In `scheduling_algorithm_api/urls.py`, define endpoints specific to scheduling algorithm interactions. ✅ udah

10. **Views and Serializers:**
    - Implement views and serializers for each endpoint in both `scheduling_api` and `scheduling_algorithm_api`. ☑️ (kurang lebih udah sih, tinggal dirapihin lagi aja, teragntung apakah ada yang mesti dikembangin lagi di algoritmanya)

11. **API Authentication and Permissions:**
    - Implement authentication mechanisms for API access (Token, JWT, OAuth, etc.).
    - Set permissions to restrict access to authorized users.

12. **Algorithm Integration:**
    - Integrate scheduling algorithm with the views in the `scheduling_algorithm_api` app. ✅ Loh udah?

13. **Testing and Debugging:**
    - Test your API endpoints using tools like Postman or `curl`.
    - Debug any issues in the algorithm integration and API interactions.

**Phase 4: Refinement and Documentation**

14. **Algorithm Tuning:**
    - Experiment with different algorithm parameters to find optimal values.
    - Fine-tune genetic operators, neighborhood moves, and tabu list management.

15. **Performance Evaluation:**
    - Evaluate algorithm's performance using sample data and real-world scenarios.
    - Compare results against benchmarks or existing scheduling methods.

16. **Documentation:**
    - Create detailed documentation for your project, including:
      - API documentation with clear explanations of endpoints and expected inputs/outputs.
      - Algorithm documentation describing its design, components, and parameter tuning.

**Phase 5: Deployment and Presentation**

17. **Deployment:**
    - Deploy Django project to a server or cloud platform (Heroku, AWS, etc.).
    - Set up databases, environment variables, and other configurations.
    - Design and implement front-end user interface using react or other framework.

18. **Monitoring and Scaling:**
    - Implement monitoring for your API service to track performance and identify issues.
    - Consider strategies for scaling service if needed.

19. **Thesis Presentation:**
    - Prepare a well-structured thesis document that covers all aspects of project.
    - Create a compelling presentation for thesis defense.

**Phase 6: Finalizing and Submission**

20. **Final Testing:**
    - Conduct thorough testing of your deployed system in a real environment.

21. **User Feedback and Refinement:**
    - Gather feedback from users or mentors.
    - Make any necessary refinements to improve the system's usability and performance.

22. **Submission:**
    - Submit completed project and thesis according to university's guidelines.
   
**Forgotten Phase: Front End.**

23. **Front-end Technology Selection:**
    - Confirm your choice of Next.js for the front end. ✅
    - Explore any additional libraries or frameworks you might need (React, Redux, etc.). ✅ (Ganti make vue jadinya)

24. **Project Setup:**
    - Install Next.js in your project directory. ✅ (Pake vue)
    - Set up the basic structure for your front-end application. ✅

25. **API Integration:**
    - Connect your Next.js application to the Django backend using API endpoints. ✅ (Pake vue)
    - Implement functions to fetch and send data to the Django API. ✅

26. **User Interface Design:**
    - Design the user interface for the timetabling system. (Baru sampe crud)
    - Consider the user experience and ensure intuitive navigation. ✅

27. **Component Implementation:**
    - Create React components for different sections of your timetabling system.
    - Implement state management if needed (Redux, React Context API). ✅ (Pake pinia)

28. **Responsive Design:**
    - Ensure your front-end is responsive and works well on various devices. ✅
    - Test the user interface on different screen sizes. ✅

29. **Testing:**
    - Perform thorough testing of your front-end components.
    - Check for any issues related to data fetching, rendering, and user interactions.

30. **Integration with Backend:**
    - Test the integration between the Next.js front end and Django backend.
    - Ensure seamless communication and data flow between the two.

31. **Optimization:**
    - Optimize your front-end code for performance.
    - Consider code splitting, lazy loading, and other optimization techniques.

32. **User Acceptance Testing:**
    - Conduct user acceptance testing with potential users or stakeholders.
    - Gather feedback on the usability and functionality of the front-end.

33. **Refinement:**
    - Make necessary refinements based on user feedback.
    - Address any issues or improvements identified during testing.

Duh banyak banget ya ternyataa .............. 🫠🫠🫠🫠.·´¯`(>▂<)´¯`·. .·´¯`(>▂<)´¯`·. .·´¯`(>▂<)´¯`·. .·´¯`(>▂<)´¯`·. இ௰இ

