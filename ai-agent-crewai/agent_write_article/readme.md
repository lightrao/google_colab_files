# AI Agent Crew for Researching and Writing Articles

This project demonstrates using the `crewai` framework to create a team of AI agents that collaborate to research a topic, write an article, and edit it.

## Workflow

The process involves three specialized agents working sequentially:

1.  **Planner:** Researches the given topic, identifies trends, target audience, and creates a detailed content outline with SEO keywords.
2.  **Writer:** Takes the planner's outline and crafts a compelling, factually accurate blog post, incorporating SEO keywords and ensuring proper structure and tone.
3.  **Editor:** Reviews the writer's draft for grammatical errors, alignment with organizational style, journalistic best practices, and balanced viewpoints.

## Agents

-   **Content Planner:** Responsible for planning engaging and factually accurate content.
-   **Content Writer:** Writes insightful opinion pieces based on the planner's outline.
-   **Editor:** Edits the blog post for quality, style, and adherence to best practices.

## Tasks

-   **Plan:** Develop a comprehensive content plan including outline, audience analysis, SEO keywords, and resources.
-   **Write:** Craft a compelling blog post based on the plan, ensuring structure, engagement, and proofreading.
-   **Edit:** Proofread the post for grammar, style alignment, and overall quality.

## How to Run

The core logic is in the `L2_research_write_article.ipynb` Jupyter Notebook.

1.  **Prerequisites:** Install the required libraries:
    ```bash
    pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29 numpy==1.25.2
    ```
    *(Note: The notebook includes specific numpy version installation, likely due to compatibility requirements.)*
2.  **API Key:** Set up your OpenAI API key. The notebook retrieves it using `userdata.get('OPENAI_API_KEY')` for Google Colab or expects the `OPENAI_API_KEY` environment variable. It defaults to using `gpt-3.5-turbo`.
3.  **Execute Notebook:** Open and run the cells in `L2_research_write_article.ipynb`. It defines the agents and tasks, creates the crew, and kicks off the process with the topic "Artificial Intelligence". You can modify the `topic` variable to generate articles on other subjects.

The notebook also includes examples of how to configure the agents to use other LLMs like Hugging Face Hub, Mistral API, or Cohere.
