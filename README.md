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
   - Design hybrid meta-heuristics algorithm (Genetic Algorithm + Tabu Search). 😭😭😭😭😭
   - Define the fitness function that evaluates schedule quality. ✅

6. **Algorithm Implementation:**
   - Create a separate module or package for scheduling algorithm.
   - Implement the Genetic Algorithm and Tabu Search components.
   - Implement genetic operators (crossover, mutation) and neighborhood moves for Tabu Search.

**Phase 3: API Development**

7. **Django Project Setup:**
   - Create a new Django project using `django-admin startproject project_name`.

8. **Create Apps:**
   - Create separate apps for different aspects of your project:
     - `scheduling_api` for general system functionality.
     - `scheduling_algorithm` for the scheduling algorithm.
     - `scheduling_algorithm_api` for scheduling algorithm-related API.

9. **Define API Endpoints:**
   - In `scheduling_api/urls.py`, define endpoints for submitting data and retrieving schedules.
   - In `scheduling_algorithm_api/urls.py`, define endpoints specific to scheduling algorithm interactions.

10. **Views and Serializers:**
    - Implement views and serializers for each endpoint in both `scheduling_api` and `scheduling_algorithm_api`.

11. **API Authentication and Permissions:**
    - Implement authentication mechanisms for API access (Token, JWT, OAuth, etc.).
    - Set permissions to restrict access to authorized users.

12. **Algorithm Integration:**
    - Integrate scheduling algorithm with the views in the `scheduling_algorithm_api` app.

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

