Of course. Here is a detailed checklist of tiny, actionable tasks for each development ticket, following a Test-Driven Development (TDD) methodology.

### **Epic: BUX-EPIC-1 \- Core Infrastructure & Aggregation MVP**

#### **BUX-001: Initial Project Setup and Configuration**

* \[ \] BUX-001-T01: Create a new Django project using django-admin startproject.  
* \[ \] BUX-001-T02: Initialize a new git repository in the project root.  
* \[ \] BUX-001-T03: Create a .gitignore file with standard Python/Django exclusions.  
* \[ \] BUX-001-T04: Create a Python virtual environment using python \-m venv venv.  
* \[ \] BUX-001-T05: Activate the virtual environment and add Django to a requirements.txt file.  
* \[ \] BUX-001-T06: Install dependencies using pip install \-r requirements.txt.  
* \[ \] BUX-001-T07: Run the initial python manage.py migrate command.  
* \[ \] BUX-001-T08: Execute python manage.py runserver to confirm the default site loads successfully.  
* \[ \] BUX-001-T09: Create a README.md file with clear, step-by-step instructions for local setup.

#### **BUX-002: Set up and Configure PostgreSQL Database**

* \[ \] BUX-002-T01: Write a test in tests.py to assert that the default database engine is django.db.backends.postgresql.  
* \[ \] BUX-002-T02: Add psycopg2-binary to requirements.txt and run pip install \-r requirements.txt.  
* \[ \] BUX-002-T03: Create a new local PostgreSQL database and user for the project.  
* \[ \] BUX-002-T04: Configure the DATABASES setting in settings.py to connect to the new PostgreSQL database. Use environment variables for sensitive credentials.  
* \[ \] BUX-002-T05: Run python manage.py test to confirm the test from T01 now passes.  
* \[ \] BUX-002-T06: Run python manage.py migrate to apply the initial Django migrations to the PostgreSQL database.

#### **BUX-003: Implement Core Data Models for Aggregation**

* \[ \] BUX-003-T01: Write unit tests for the Source model, covering field types, constraints (e.g., url is unique), and the \_\_str\_\_ method.  
* \[ \] BUX-003-T02: Create the Source model in a new core/models.py file.  
* \[ \] BUX-003-T03: Write unit tests for the AggregatedContent model, testing its fields and the foreign key relationship to Source.  
* \[ \] BUX-003-T04: Create the AggregatedContent model.  
* \[ \] BUX-003-T05: Write unit tests for the ProcessedContent model, testing its fields and the one-to-one relationship to AggregatedContent.  
* \[ \] BUX-003-T06: Create the ProcessedContent model.  
* \[ \] BUX-003-T07: Run python manage.py makemigrations.  
* \[ \] BUX-003-T08: Run python manage.py migrate.  
* \[ \] BUX-003-T09: Register the new models in core/admin.py.  
* \[ \] BUX-003-T10: Run and pass all model unit tests created in this ticket.

#### **BUX-004: Integrate Celery and Redis for Asynchronous Tasks**

* \[ \] BUX-004-T01: Write a unit test that calls .delay() on a mock task and asserts it was queued.  
* \[ \] BUX-004-T02: Add celery and redis to requirements.txt and install.  
* \[ \] BUX-004-T03: Create a celery.py file in the main project directory.  
* \[ \] BUX-004-T04: Update the project's \_\_init\_\_.py to ensure the Celery app is loaded.  
* \[ \] BUX-004-T05: Configure CELERY\_BROKER\_URL and CELERY\_RESULT\_BACKEND in settings.py.  
* \[ \] BUX-004-T06: Create a core/tasks.py file and define a simple @shared\_task for testing.  
* \[ \] BUX-004-T07: Run the Celery worker locally to confirm it connects to Redis.  
* \[ \] BUX-004-T08: Run and pass the unit test from T01.

#### **BUX-005: Develop Initial Scrapy Spiders for RSS Feeds**

* \[ \] BUX-005-T01: Write a unit test for the spider's parsing method, using a mock response object to simulate an RSS feed. Assert that the correct data is extracted.  
* \[ \] BUX-005-T02: Add scrapy to requirements.txt and install.  
* \[ \] BUX-005-T03: Create a new Scrapy project structure within the Django app (or alongside).  
* \[ \] BUX-005-T04: Implement the RSS spider, writing the parsing logic to extract fields.  
* \[ \] BUX-005-T05: Implement a Scrapy Item Pipeline that saves the extracted item to the AggregatedContent model.  
* \[ \] BUX-005-T06: Run and pass the unit test from T01.

#### **BUX-006: Build Content Processing Pipeline with Celery**

* \[ \] BUX-006-T01: Write unit tests for the processing logic: one for HTML tag stripping, one for date string parsing, and one for text normalization.  
* \[ \] BUX-006-T02: Add beautifulsoup4 and python-dateutil to requirements.txt and install.  
* \[ \] BUX-006-T03: Create a new Celery task in core/tasks.py called process\_content\_task.  
* \[ \] BUX-006-T04: Implement the cleaning and normalization logic within the task, using the libraries from T02.  
* \[ \] BUX-006-T05: Add logic to the task to create and save a ProcessedContent instance from the cleaned data.  
* \[ \] BUX-006-T06: Implement logic in the Scrapy pipeline from BUX-005-T05 to dispatch this new Celery task upon saving AggregatedContent.  
* \[ \] BUX-006-T07: Run and pass all unit tests from T01.

#### **BUX-007: Schedule Aggregation Tasks with Celery Beat**

* \[ \] BUX-007-T01: Write a test to ensure the Celery Beat schedule configuration is loaded correctly in the Django settings.  
* \[ \] BUX-007-T02: Configure a basic schedule in settings.py for Celery Beat to run a test task.  
* \[ \] BUX-007-T03: Implement a periodic task that queries for active Source objects and dispatches individual scraping jobs for each.  
* \[ \] BUX-007-T04: Run Celery Beat locally to confirm that tasks are being scheduled and sent to the broker.  
* \[ \] BUX-007-T05: Run and pass the test from T01.

#### **BUX-008: Create Basic Frontend to Display Aggregated Content**

* \[ \] BUX-008-T01: Write a Django view test to check that a GET request to / returns a 200 status code.  
* \[ \] BUX-008-T02: Write a test to ensure the view's context contains a list of ProcessedContent objects.  
* \[ \] BUX-008-T03: Create a ProcessedContentListView in core/views.py.  
* \[ \] BUX-008-T04: Create a corresponding URL pattern in urls.py.  
* \[ \] BUX-008-T05: Create an HTML template (processedcontent\_list.html) that iterates through the content list and displays the title and a link to the original source.  
* \[ \] BUX-008-T06: Run and pass all tests for the view.

### **Epic: BUX-EPIC-2 \- AI Content Generation & Distribution MVP**

#### **BUX-009: Integrate with a Proprietary LLM API**

* \[ \] BUX-009-T01: Write a unit test for an API service module, using unittest.mock.patch to mock the external API call and test the wrapper's behavior.  
* \[ \] BUX-009-T02: Add the required SDK (e.g., openai) to requirements.txt and install.  
* \[ \] BUX-009-T03: Create a new file, core/services.py, to encapsulate all interactions with the LLM API.  
* \[ \] BUX-009-T04: Implement a function to securely load the API key from an environment variable.  
* \[ \] BUX-009-T05: Implement the wrapper function that constructs the API request and handles the response.  
* \[ \] BUX-009-T06: Run and pass the mocked unit test from T01.

#### **BUX-010: Implement AI-Generated Content Models**

* \[ \] BUX-010-T01: Write unit tests for the GeneratedArticle model, testing its fields, status choices, and ManyToMany relationship with ProcessedContent.  
* \[ \] BUX-010-T02: Implement the GeneratedArticle model in core/models.py.  
* \[ \] BUX-010-T03: Run makemigrations and migrate.  
* \[ \] BUX-010-T04: Register the model in core/admin.py.  
* \[ \] BUX-010-T05: Run and pass all GeneratedArticle model tests.

#### **BUX-011: Develop Celery Task for AI Content Summarization**

* \[ \] BUX-011-T01: Write a unit test for the summarization task, mocking the database query and the LLM API call (core/services.py).  
* \[ \] BUX-011-T02: Create a new task generate\_summary\_task in core/tasks.py.  
* \[ \] BUX-011-T03: Implement logic to query for recent ProcessedContent.  
* \[ \] BUX-011-T04: Implement prompt engineering logic to construct a detailed prompt.  
* \[ \] BUX-011-T05: Implement the call to the LLM service from BUX-009.  
* \[ \] BUX-011-T06: Implement logic to save the API response into a new GeneratedArticle instance.  
* \[ \] BUX-011-T07: Add the new task to the Celery Beat schedule in settings.py.  
* \[ \] BUX-011-T08: Run and pass the unit test from T01.

#### **BUX-012: Display Generated Articles on the Frontend**

* \[ \] BUX-012-T01: Write tests for a list view (GeneratedArticleListView) ensuring it returns a 200 code and filters for 'published' articles.  
* \[ \] BUX-012-T02: Write tests for a detail view (GeneratedArticleDetailView) ensuring it returns a 200 code for a valid slug/ID and a 404 for an invalid one.  
* \[ \] BUX-012-T03: Implement the GeneratedArticleListView and GeneratedArticleDetailView in core/views.py.  
* \[ \] BUX-012-T04: Create URL patterns for both views.  
* \[ \] BUX-012-T05: Create templates for the list (generatedarticle\_list.html) and detail (generatedarticle\_detail.html) views.  
* \[ \] BUX-012-T06: Run and pass all view tests.

#### **BUX-013: Implement RSS Feed for Generated Content**

* \[ \] BUX-013-T01: Write a Django client test to make a GET request to the feed URL and assert it returns a 200 code and has an application/rss+xml content type.  
* \[ \] BUX-013-T02: Create a feeds.py file in the core app.  
* \[ \] BUX-013-T03: Implement a LatestArticlesFeed class using Django's syndication framework.  
* \[ \] BUX-013-T04: Add the URL pattern for the feed to urls.py.  
* \[ \] BUX-013-T05: Run and pass the test from T01.

### **Epic: BUX-EPIC-3 \- Community Forum MVP**

#### **BUX-014: Implement Core Forum and User Profile Models**

* \[ \] BUX-014-T01: Write unit tests for ForumCategory, ForumTopic, ForumPost, and UserProfile models.  
* \[ \] BUX-014-T02: Create a new Django app called forum.  
* \[ \] BUX-014-T03: Implement the forum-related models in forum/models.py.  
* \[ \] BUX-014-T04: Run makemigrations and migrate.  
* \[ \] BUX-014-T05: Register models in forum/admin.py.  
* \[ \] BUX-014-T06: Run and pass all forum model tests.

#### **BUX-015: Build User Authentication and Profile Management**

* \[ \] BUX-015-T01: Write tests for the registration view, login view, and profile update view, checking for correct redirection and form handling.  
* \[ \] BUX-015-T02: Create a new Django app called accounts.  
* \[ \] BUX-015-T03: Implement views and forms for user registration, login, and logout using Django's built-in components.  
* \[ \] BUX-015-T04: Create a UserProfile view and form for editing profile data.  
* \[ \] BUX-015-T05: Create all necessary URL patterns and templates.  
* \[ \] BUX-015-T06: Run and pass all auth and profile tests.

#### **BUX-016: Develop Forum Views and Navigation using HTMX**

* \[ \] BUX-016-T01: Write view tests for the forum category list, topic list, and topic detail pages.  
* \[ \] BUX-016-T02: Add django-htmx to requirements.txt and install. Configure middleware.  
* \[ \] BUX-016-T03: Implement the required class-based views in forum/views.py.  
* \[ \] BUX-016-T04: Create the URL patterns in forum/urls.py.  
* \[ \] BUX-016-T05: Build the HTML templates for each view, incorporating HTMX attributes for future dynamic actions.  
* \[ \] BUX-016-T06: Run and pass all forum view tests.

#### **BUX-017: Implement Topic and Reply Creation Functionality**

* \[ \] BUX-017-T01: Write tests for the CreateTopicView and CreatePostView, simulating POST requests with valid and invalid data. Test that login is required.  
* \[ \] BUX-017-T02: Create TopicCreateForm and PostCreateForm in forum/forms.py.  
* \[ \] BUX-017-T03: Implement the views for creating topics and replies. The reply view should handle HTMX requests, returning only a partial template fragment.  
* \[ \] BUX-017-T04: Integrate the forms into the topic list and topic detail templates.  
* \[ \] BUX-017-T05: Write the HTMX JavaScript to handle form submission for replies.  
* \[ \] BUX-017-T06: Run and pass all form and view creation tests.