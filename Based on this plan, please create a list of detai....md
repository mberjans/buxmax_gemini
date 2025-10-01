Of course. Here is a detailed list of software development tickets for the Buxmax project, presented in a Jira-like format and adhering to the "no Docker" constraint.

### **Epic: BUX-EPIC-1 \- Core Infrastructure & Aggregation MVP**

This epic covers the foundational setup of the project, including the core application, database, asynchronous task processing, and the basic data aggregation pipeline.

---

Ticket ID: BUX-001  
Title: Initial Project Setup and Configuration  
Description: Initialize the Django project, set up the project structure, and establish the local development environment using Python's venv. Configure basic settings for development.  
Acceptance Criteria:

1. A new Django project is created.  
2. A requirements.txt file is created with initial dependencies (Django, Psycopg2).  
3. A local development environment can be set up using python \-m venv and pip install \-r requirements.txt.  
4. The Django development server runs successfully.  
   Dependencies: None  
   Independent: Yes

---

Ticket ID: BUX-002  
Title: Set up and Configure PostgreSQL Database  
Description: Install PostgreSQL locally for development and configure the Django project to connect to it. Document the setup process for new developers.  
Acceptance Criteria:

1. Django settings are configured to use PostgreSQL.  
2. The project successfully connects to a local PostgreSQL instance.  
3. Running python manage.py migrate executes successfully.  
   Dependencies: BUX-001  
   Independent: No

---

Ticket ID: BUX-003  
Title: Implement Core Data Models for Aggregation  
Description: Create the initial Django ORM models required for storing aggregated content as defined in section 4.1 of the development plan. This includes Source, AggregatedContent, and ProcessedContent.  
Acceptance Criteria:

1. The Source, AggregatedContent, and ProcessedContent models are created with all specified fields.  
2. Database migrations are generated and applied successfully.  
3. Models are registered in the Django admin site for basic data management.  
   Dependencies: BUX-002  
   Independent: No

---

Ticket ID: BUX-004  
Title: Integrate Celery and Redis for Asynchronous Tasks  
Description: Set up Celery for managing background tasks and configure Redis as the message broker and result backend. Ensure Celery workers can be run alongside the Django development server.  
Acceptance Criteria:

1. Celery and Redis are added to requirements.txt.  
2. The Django project is configured to use Celery with Redis.  
3. A sample asynchronous task (@shared\_task) can be created and executed successfully by a Celery worker.  
4. Local development instructions are updated for running Celery workers.  
   Dependencies: BUX-001  
   Independent: No

---

Ticket ID: BUX-005  
Title: Develop Initial Scrapy Spiders for RSS Feeds  
Description: Create a Scrapy spider capable of parsing standard RSS and Atom feeds. The spider should be designed to take a source URL as input and extract relevant data.  
Acceptance Criteria:

1. A Scrapy spider is created that can parse an RSS feed URL.  
2. The spider extracts the title, link, publication date, and content body for each item in the feed.  
3. The extracted data is saved to the AggregatedContent model.  
   Dependencies: BUX-003  
   Independent: No

---

Ticket ID: BUX-006  
Title: Build Content Processing Pipeline with Celery  
Description: Create Celery tasks to process raw data from AggregatedContent. This pipeline should perform data cleaning (HTML stripping), normalization (whitespace, date parsing), and save the result to the ProcessedContent model.  
Acceptance Criteria:

1. A Celery task is created that takes an AggregatedContent ID as input.  
2. The task cleans the raw HTML content, normalizes text, and parses the publication date.  
3. A new ProcessedContent object is created and linked to the source AggregatedContent object.  
   Dependencies: BUX-003, BUX-004  
   Independent: No

---

Ticket ID: BUX-007  
Title: Schedule Aggregation Tasks with Celery Beat  
Description: Configure Celery Beat to periodically trigger the scraping tasks. The schedule should be configurable based on the scrape\_frequency field in the Source model.  
Acceptance Criteria:

1. Celery Beat is configured in the project.  
2. A periodic task is set up to query Source models and dispatch scraping jobs to Celery workers based on their individual schedules.  
3. The scheduling process can be monitored locally.  
   Dependencies: BUX-005, BUX-006  
   Independent: No

---

Ticket ID: BUX-008  
Title: Create Basic Frontend to Display Aggregated Content  
Description: Develop a simple Django view and template to display a list of titles from the ProcessedContent table. Each title should link to the original source URL. Use standard Django templates and HTMX for this initial phase.  
Acceptance Criteria:

1. A Django view fetches all ProcessedContent objects.  
2. An HTML template renders the content as a list.  
3. The page displays the title of each processed article.  
4. Each title links to the original url stored in the related AggregatedContent model.  
   Dependencies: BUX-006  
   Independent: No

### **Epic: BUX-EPIC-2 \- AI Content Generation & Distribution MVP**

This epic focuses on integrating AI to generate unique content from the aggregated data and making that content available via the web and an RSS feed. This completes the MVP.

---

Ticket ID: BUX-009  
Title: Integrate with a Proprietary LLM API  
Description: Set up the Python SDK for the chosen LLM (e.g., OpenAI or Anthropic). Implement a secure way to manage API keys using environment variables (not committed to source control). Create a service or utility module for interacting with the API.  
Acceptance Criteria:

1. The selected LLM's Python SDK is added to requirements.txt.  
2. A wrapper/service class is created to handle API calls.  
3. API keys are loaded securely from environment variables.  
4. A test function can successfully make a simple completion call to the API.  
   Dependencies: BUX-001  
   Independent: Yes

---

Ticket ID: BUX-010  
Title: Implement AI-Generated Content Models  
Description: Create the GeneratedArticle model as defined in section 4.1. This model will store the AI-generated summaries and articles, including references to the source content used.  
Acceptance Criteria:

1. The GeneratedArticle model is created with fields for title, body, status, and a ManyToMany relationship to ProcessedContent.  
2. Database migrations are generated and applied.  
3. The model is registered in the Django admin.  
   Dependencies: BUX-003  
   Independent: No

---

Ticket ID: BUX-011  
Title: Develop Celery Task for AI Content Summarization  
Description: Create a scheduled Celery task that gathers recent ProcessedContent items, constructs a prompt, and uses the LLM API to generate a summary. The result should be saved as a GeneratedArticle.  
Acceptance Criteria:

1. A Celery task is created that can be triggered by Celery Beat.  
2. The task selects one or more recent ProcessedContent items.  
3. A prompt is engineered to request an abstractive summary (as per section 6.3).  
4. The generated summary is saved as a new GeneratedArticle in 'draft' status.  
   Dependencies: BUX-009, BUX-010  
   Independent: No

---

Ticket ID: BUX-012  
Title: Display Generated Articles on the Frontend  
Description: Create a new Django view and template to display published GeneratedArticle content. Create a detail view to show the full body of a single article.  
Acceptance Criteria:

1. A list view displays all GeneratedArticle instances with a 'published' status.  
2. A detail view displays the title and body of a single GeneratedArticle.  
3. Templates are clean and readable.  
   Dependencies: BUX-010  
   Independent: No

---

Ticket ID: BUX-013  
Title: Implement RSS Feed for Generated Content  
Description: Use Django's syndication feed framework to create an RSS feed of the most recent GeneratedArticle entries. This will serve as the final piece of the MVP for content distribution.  
Acceptance Criteria:

1. An RSS feed is available at a designated URL (e.g., /latest/feed/).  
2. The feed contains the 10-20 most recent 'published' GeneratedArticles.  
3. The feed validates correctly according to RSS standards.  
   Dependencies: BUX-012  
   Independent: No

### **Epic: BUX-EPIC-3 \- Community Forum MVP**

This epic covers the development of a functional, human-only community forum.

---

Ticket ID: BUX-014  
Title: Implement Core Forum and User Profile Models  
Description: Create the ForumCategory, ForumTopic, ForumPost, and extended UserProfile models as defined in section 4.1.  
Acceptance Criteria:

1. All specified forum and profile models are created.  
2. Relationships (ForeignKeys, etc.) between models are correctly defined.  
3. Database migrations are generated and applied successfully.  
   Dependencies: BUX-003 (for the User model)  
   Independent: No

---

Ticket ID: BUX-015  
Title: Build User Authentication and Profile Management  
Description: Implement user registration, login, logout, and password reset flows using Django's built-in authentication system. Create views for users to view and edit their UserProfile.  
Acceptance Criteria:

1. Users can create a new account with email verification.  
2. Registered users can log in and log out.  
3. Logged-in users can view their profile and update fields like 'bio'.  
   Dependencies: BUX-014  
   Independent: No

---

Ticket ID: BUX-016  
Title: Develop Forum Views and Navigation using HTMX  
Description: Create the main views for the forum: a category list, a topic list within a category, and a topic detail page showing all posts. Use HTMX to handle interactions like posting a reply without a full page reload.  
Acceptance Criteria:

1. Users can navigate from the category list to a topic list, and then to a topic detail page.  
2. The topic detail page correctly displays the initial post and all replies in chronological order.  
3. HTMX is integrated for a smoother user experience.  
   Dependencies: BUX-014  
   Independent: No

---

Ticket ID: BUX-017  
Title: Implement Topic and Reply Creation Functionality  
Description: Create the forms and views necessary for logged-in users to create new topics within a category and to post replies to existing topics.  
Acceptance Criteria:

1. A logged-in user can successfully create a new topic in a valid category.  
2. A logged-in user can post a reply to an existing topic.  
3. The creator of the topic/post is correctly associated with their user account.  
4. Posting a reply via HTMX updates the topic page dynamically.  
   Dependencies: BUX-015, BUX-016  
   Independent: No