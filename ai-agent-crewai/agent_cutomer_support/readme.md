# Multi-Agent Customer Support Automation with crewAI

This project demonstrates how to build a multi-agent customer support system using the `crewai` library. It illustrates key concepts for enhancing agent performance:

-   **Role Playing:** Defining specific roles, goals, and backstories for agents.
-   **Focus:** Prompting agents to embody their assigned roles.
-   **Tools:** Equipping agents with tools like web scraping (`ScrapeWebsiteTool`) and search (`SerperDevTool`) to access external information. The notebook uses a `ScrapeWebsiteTool` configured to scrape CrewAI documentation.
-   **Cooperation:** Enabling agents to delegate tasks and work together.
-   **Guardrails:** Ensuring agent responses stay within the expected scope.
-   **Memory:** Allowing the crew to retain information across interactions by setting `memory=True`.

## Agents

1.  **Senior Support Representative:** A friendly and helpful agent responsible for addressing customer inquiries thoroughly.
2.  **Support Quality Assurance Specialist:** An agent focused on reviewing the support representative's responses for completeness, accuracy, and tone.

## Tasks

1.  **Inquiry Resolution:** The support representative uses available tools (specifically, the documentation scraper) to answer a customer's question.
2.  **Quality Assurance Review:** The QA specialist reviews the drafted response to ensure high standards are met before sending it to the customer.

## How to Run

The core logic is contained within the `L3_customer_support.ipynb` Jupyter Notebook.

1.  **Prerequisites:** Ensure you have the necessary libraries installed:
    ```bash
    pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29
    ```
2.  **API Key:** Set up your OpenAI API key. The notebook uses a utility function `get_openai_api_key()` assumed to be in a `utils` module, or you can set the `OPENAI_API_KEY` environment variable directly.
3.  **Execute Notebook:** Open and run the cells in `L3_customer_support.ipynb`. The notebook defines the agents and tasks, creates a crew, and runs it with a sample customer inquiry.

This example provides a foundation for building more complex customer support automation workflows using multiple collaborating AI agents.
