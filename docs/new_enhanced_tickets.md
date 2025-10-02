# Comprehensive Development Tickets for Frugal Living Platform

## Overview
This document contains detailed software development tickets for building a frugal living content aggregation and generation platform. Each ticket is designed to be executed autonomously by an AI coding agent without human intervention.

---

## PHASE 1: CORE INFRASTRUCTURE & AGGREGATION MVP

### TICKET-001: Project Setup and Environment Configuration
**Priority:** CRITICAL | **Phase:** 1 | **Dependencies:** None

**Description:**
Set up the foundational Django project structure with all necessary configuration files, directory structure, and development environment setup.

**Requirements:**
1. Create Django project named `buxmax_gemini` with the following structure:
   - `config/` directory for project settings (not `buxmax_gemini/`)
   - `apps/` directory for Django applications
   - `scrapers/` directory for Scrapy project
   - `static/`, `media/`, `templates/`, `logs/`, `scripts/` directories
   
2. Create `config/settings/` module with:
   - `base.py` - Base settings shared across all environments
   - `development.py` - Development-specific settings (DEBUG=True, etc.)
   - `production.py` - Production settings (DEBUG=False, security settings)
   - `testing.py` - Test-specific settings
   - `__init__.py` - Auto-detect environment and load appropriate settings

3. Create `requirements/` directory with:
   - `base.txt` - Core dependencies (Django>=4.2, psycopg2-binary, celery, redis, etc.)
   - `development.txt` - Dev dependencies (includes base.txt, adds django-debug-toolbar, ipython)
   - `production.txt` - Production dependencies (includes base.txt, adds gunicorn, sentry-sdk)
   - `testing.txt` - Testing dependencies (includes base.txt, adds pytest, pytest-django, factory-boy)

4. Create `.env.example` file with all required environment variables:
   ```
   DJANGO_SECRET_KEY=
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=postgres://user:password@localhost:5432/buxmax_db
   REDIS_URL=redis://localhost:6379/0
   CELERY_BROKER_URL=redis://localhost:6379/0
   OPENAI_API_KEY=
   ANTHROPIC_API_KEY=
   ```

5. Create `config/celery.py` for Celery configuration
6. Create `config/urls.py` for root URL configuration
7. Create `config/wsgi.py` and `config/asgi.py`
8. Create `.gitignore` with Python, Django, and IDE-specific patterns
9. Create `README.md` with project overview and setup instructions
10. Create `manage.py` pointing to config.settings

**Acceptance Criteria:**
- Django project starts successfully with `python manage.py runserver`
- Settings are properly split by environment
- All directories are created with appropriate `.gitkeep` files
- `.env.example` contains all necessary variables
- `requirements/base.txt` includes: Django>=4.2, psycopg2-binary>=2.9, celery>=5.3, redis>=5.0, python-dotenv

**Files to Create:**
- `config/__init__.py`, `config/settings/__init__.py`, `config/settings/base.py`, `config/settings/development.py`, `config/settings/production.py`, `config/settings/testing.py`
- `config/celery.py`, `config/urls.py`, `config/wsgi.py`, `config/asgi.py`
- `requirements/base.txt`, `requirements/development.txt`, `requirements/production.txt`, `requirements/testing.txt`
- `.env.example`, `.gitignore`, `README.md`, `manage.py`
- Directory structure as specified

---

### TICKET-002: Docker Configuration for Local Development
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-001

**Description:**
Create Docker and Docker Compose configuration for local development environment including Django, PostgreSQL, Redis, and Celery services.

**Requirements:**
1. Create `docker/Dockerfile` for Django application:
   - Base image: python:3.11-slim
   - Install system dependencies
   - Copy and install Python requirements
   - Set working directory to `/app`
   - Expose port 8000
   - Default command: `gunicorn config.wsgi:application --bind 0.0.0.0:8000`

2. Create `docker/Dockerfile.celery` for Celery workers:
   - Similar to main Dockerfile
   - Default command: `celery -A config worker -l info`

3. Create `docker-compose.yml` with services:
   - `db`: PostgreSQL 15 with persistent volume
   - `redis`: Redis 7 with persistent volume
   - `web`: Django application (depends on db, redis)
   - `celery_worker`: Celery worker (depends on db, redis, web)
   - `celery_beat`: Celery beat scheduler (depends on db, redis, web)
   - `flower`: Celery monitoring (depends on redis, celery_worker)

4. Configure environment variables in docker-compose.yml
5. Set up volume mounts for local development (code, static, media)
6. Configure networking between services
7. Add health checks for database and redis services

**Acceptance Criteria:**
- `docker-compose up` starts all services successfully
- Django application accessible at http://localhost:8000
- PostgreSQL accessible on port 5432
- Redis accessible on port 6379
- Flower monitoring accessible at http://localhost:5555
- Code changes reflect immediately (volume mounted)
- Database data persists between container restarts

**Files to Create:**
- `docker/Dockerfile`
- `docker/Dockerfile.celery`
- `docker-compose.yml`
- `docker/.dockerignore`

---

### TICKET-003: Core Abstract Models and Mixins
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-001

**Description:**
Create the `core` Django app with abstract base models and mixins that will be reused across the application.

**Requirements:**
1. Create `apps/core/` Django app with standard structure
2. In `apps/core/models.py`, create:
   - `TimeStampedModel` abstract model with:
     - `created_at` (DateTimeField, auto_now_add=True, db_index=True)
     - `updated_at` (DateTimeField, auto_now=True)
     - Meta: abstract=True, ordering=['-created_at']
   
   - `SoftDeleteModel` abstract model with:
     - `is_deleted` (BooleanField, default=False, db_index=True)
     - `deleted_at` (DateTimeField, null=True, blank=True)
     - `soft_delete()` method
     - `restore()` method
     - Meta: abstract=True

3. Create `apps/core/managers.py` with:
   - `SoftDeleteManager` that filters out deleted objects by default
   - `SoftDeleteQuerySet` with `delete()` override for soft deletion

4. Add comprehensive docstrings to all classes and methods
5. Create `apps/core/tests/test_models.py` with unit tests for both models

**Acceptance Criteria:**
- Core app is registered in INSTALLED_APPS
- TimeStampedModel automatically sets created_at and updated_at
- SoftDeleteModel.soft_delete() marks object as deleted without removing from DB
- SoftDeleteModel.restore() restores soft-deleted objects
- All tests pass with `pytest apps/core/tests/`

**Files to Create:**
- `apps/core/__init__.py`, `apps/core/apps.py`, `apps/core/models.py`, `apps/core/managers.py`, `apps/core/admin.py`
- `apps/core/tests/__init__.py`, `apps/core/tests/test_models.py`

---

### TICKET-004: Aggregation App - Source Model
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-003

**Description:**
Create the `aggregation` Django app and implement the `Source` model for managing external content sources.

**Requirements:**
1. Create `apps/aggregation/` Django app
2. In `apps/aggregation/models.py`, create `Source` model inheriting from `TimeStampedModel`:
   - Fields:
     - `url` (URLField, max_length=500, unique=True, with URLValidator)
     - `name` (CharField, max_length=255)
     - `description` (TextField, blank=True, default='')
     - `source_type` (CharField, choices=['rss', 'blog', 'forum', 'youtube', 'api', 'reddit'], db_index=True)
     - `feed_url` (URLField, blank=True, null=True)
     - `api_endpoint` (URLField, blank=True, null=True)
     - `scrape_frequency` (DurationField, default=timedelta(hours=24))
     - `last_checked_at` (DateTimeField, null=True, blank=True, db_index=True)
     - `last_success_at` (DateTimeField, null=True, blank=True)
     - `consecutive_failures` (IntegerField, default=0)
     - `status` (CharField, choices=['active', 'inactive', 'error', 'pending'], default='pending', db_index=True)
     - `relevance_score` (DecimalField, max_digits=3, decimal_places=2, default=0.50)
     - `target_regions` (ArrayField of CharField, default=list, blank=True)
     - `language` (CharField, max_length=10, default='en')
     - `tags` (ArrayField of CharField, default=list, blank=True)
     - `last_error` (TextField, blank=True, default='')
     - `last_error_at` (DateTimeField, null=True, blank=True)
   
   - Methods:
     - `mark_scrape_attempt(success=True, error_message='')` - Update after scrape
     - `get_effective_url()` - Return URL to use for scraping
     - `__str__()` - Return name and source_type

3. Create `SourceManager` custom manager with methods:
   - `active()` - Return only active sources
   - `due_for_scraping()` - Return sources needing scraping based on frequency

4. Add Meta class with:
   - `db_table = 'aggregation_source'`
   - `ordering = ['-relevance_score', 'name']`
   - Composite indexes on (status, last_checked_at) and (source_type, status)

5. Create `apps/aggregation/admin.py` with ModelAdmin for Source
6. Create migrations and apply them
7. Create comprehensive tests in `apps/aggregation/tests/test_models.py`

**Acceptance Criteria:**
- Source model created with all specified fields
- Custom manager methods work correctly
- `mark_scrape_attempt()` updates status to 'error' after 5 consecutive failures
- `get_effective_url()` returns feed_url for RSS, api_endpoint for API, else url
- Admin interface allows CRUD operations on Source
- All tests pass
- Migrations apply successfully

**Files to Create:**
- `apps/aggregation/__init__.py`, `apps/aggregation/apps.py`, `apps/aggregation/models.py`, `apps/aggregation/admin.py`
- `apps/aggregation/migrations/0001_initial.py`
- `apps/aggregation/tests/__init__.py`, `apps/aggregation/tests/test_models.py`, `apps/aggregation/tests/factories.py`

---

### TICKET-005: Aggregation App - AggregatedContent Model
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-004

**Description:**
Implement the `AggregatedContent` model for storing raw content fetched from sources.

**Requirements:**
1. In `apps/aggregation/models.py`, create `AggregatedContent` model inheriting from `TimeStampedModel`:
   - Fields:
     - `source` (ForeignKey to Source, on_delete=CASCADE, related_name='aggregated_content')
     - `url` (URLField, max_length=1000, unique=True)
     - `content_hash` (CharField, max_length=64, unique=True, db_index=True)
     - `title` (CharField, max_length=500)
     - `content_body` (TextField)
     - `content_type` (CharField, choices=['article', 'post', 'video', 'podcast', 'other'], default='article', db_index=True)
     - `author` (CharField, max_length=255, blank=True, default='')
     - `published_at` (DateTimeField, null=True, blank=True, db_index=True)
     - `fetched_at` (DateTimeField, auto_now_add=True, db_index=True)
     - `raw_data` (JSONField, default=dict, blank=True)
     - `is_processed` (BooleanField, default=False, db_index=True)
   
   - Methods:
     - `generate_content_hash()` - Generate SHA-256 hash for deduplication
     - `save()` - Override to auto-generate content_hash
     - `__str__()` - Return title and source name

2. Add Meta class with:
   - `db_table = 'aggregation_content'`
   - `ordering = ['-published_at', '-fetched_at']`
   - Composite indexes on (source, published_at), (is_processed, fetched_at), (content_type, published_at)

3. Update `apps/aggregation/admin.py` to include AggregatedContent
4. Create and apply migrations
5. Add tests for content hash generation and deduplication

**Acceptance Criteria:**
- AggregatedContent model created with all fields
- Content hash automatically generated on save
- Duplicate content (same hash) raises IntegrityError
- Admin interface shows aggregated content with filters
- Tests verify hash generation and uniqueness constraints
- Migrations apply successfully

**Files to Modify:**
- `apps/aggregation/models.py`
- `apps/aggregation/admin.py`

**Files to Create:**
- `apps/aggregation/migrations/0002_aggregatedcontent.py`
- `apps/aggregation/tests/test_aggregated_content.py`

---

### TICKET-006: Content App - ProcessedContent Model
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-005

**Description:**
Create the `content` Django app and implement the `ProcessedContent` model for storing cleaned and structured content.

**Requirements:**
1. Create `apps/content/` Django app
2. In `apps/content/models.py`, create `ProcessedContent` model inheriting from `TimeStampedModel`:
   - Fields:
     - `aggregated_content` (OneToOneField to AggregatedContent, on_delete=CASCADE, related_name='processed')
     - `cleaned_title` (CharField, max_length=500)
     - `summary` (TextField, blank=True, default='')
     - `cleaned_body` (TextField)
     - `keywords` (ArrayField of CharField max_length=100, default=list, blank=True)
     - `entities` (JSONField, default=dict, blank=True)
     - `sentiment_score` (DecimalField, max_digits=3, decimal_places=2, null=True, blank=True)
     - `word_count` (IntegerField, default=0)
     - `reading_time_minutes` (IntegerField, default=0)
     - `processed_at` (DateTimeField, auto_now_add=True)
     - `processing_version` (CharField, max_length=20, default='1.0')

   - Methods:
     - `calculate_reading_time()` - Calculate reading time (word_count // 200)
     - `__str__()` - Return cleaned title

3. Add Meta class with:
   - `db_table = 'content_processed'`
   - `ordering = ['-processed_at']`
   - Index on processed_at

4. Create admin interface for ProcessedContent
5. Create and apply migrations
6. Create tests for the model

**Acceptance Criteria:**
- ProcessedContent model created with all fields
- One-to-one relationship with AggregatedContent works correctly
- `calculate_reading_time()` correctly calculates minutes (min 1 minute)
- Admin interface functional
- Tests pass
- Migrations apply successfully

**Files to Create:**
- `apps/content/__init__.py`, `apps/content/apps.py`, `apps/content/models.py`, `apps/content/admin.py`
- `apps/content/migrations/0001_initial.py`
- `apps/content/tests/__init__.py`, `apps/content/tests/test_models.py`, `apps/content/tests/factories.py`

---

### TICKET-007: Celery Configuration and Basic Tasks
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-002

**Description:**
Configure Celery for asynchronous task processing and create basic task infrastructure.

**Requirements:**
1. In `config/celery.py`, configure Celery:
   - Set broker_url from environment variable
   - Set result_backend to Redis
   - Configure task serialization (JSON)
   - Set timezone to UTC
   - Enable task result expiration (24 hours)
   - Configure task routes if needed

2. In `config/__init__.py`, ensure Celery app is loaded:
   ```python
   from .celery import app as celery_app
   __all__ = ('celery_app',)
   ```

3. Create `apps/core/tasks.py` with example tasks:
   - `test_celery_task()` - Simple test task that returns success message
   - `cleanup_old_logs()` - Task to clean up old log files

4. Configure Celery Beat schedule in settings for periodic tasks:
   - Add CELERY_BEAT_SCHEDULE dictionary
   - Schedule cleanup task to run daily

5. Create management command `apps/core/management/commands/test_celery.py`:
   - Command to test Celery connectivity
   - Dispatches test task and waits for result

6. Update requirements to include:
   - celery[redis]>=5.3
   - django-celery-results>=2.5
   - django-celery-beat>=2.5

7. Configure django-celery-results in settings:
   - Add to INSTALLED_APPS
   - Set CELERY_RESULT_BACKEND to use Django ORM

**Acceptance Criteria:**
- Celery worker starts successfully: `celery -A config worker -l info`
- Celery beat starts successfully: `celery -A config beat -l info`
- Test task executes and returns result
- Management command successfully dispatches and receives task result
- Flower monitoring shows tasks and workers
- Periodic tasks are scheduled correctly

**Files to Create:**
- `apps/core/tasks.py`
- `apps/core/management/__init__.py`
- `apps/core/management/commands/__init__.py`
- `apps/core/management/commands/test_celery.py`

**Files to Modify:**
- `config/celery.py`
- `config/__init__.py`
- `config/settings/base.py` (add Celery configuration)
- `requirements/base.txt`

---

### TICKET-008: Basic Scrapy Project Setup
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-005

**Description:**
Set up the Scrapy project structure for web scraping with Django integration.

**Requirements:**
1. Create `scrapers/` directory with Scrapy project structure:
   - `scrapy.cfg` - Scrapy configuration file
   - `__init__.py`
   - `settings.py` - Scrapy settings
   - `items.py` - Item definitions
   - `pipelines.py` - Processing pipelines
   - `middlewares.py` - Custom middlewares
   - `spiders/__init__.py`

2. In `scrapers/settings.py`, configure:
   - BOT_NAME = 'buxmax_scrapers'
   - ROBOTSTXT_OBEY = True
   - CONCURRENT_REQUESTS = 16
   - DOWNLOAD_DELAY = 1
   - USER_AGENT rotation
   - ITEM_PIPELINES with Django integration pipeline
   - Configure Django settings module
   - Enable AutoThrottle extension

3. In `scrapers/items.py`, define:
   - `ContentItem` with fields: url, title, content_body, author, published_at, source_url, content_type, raw_data

4. In `scrapers/pipelines.py`, create:
   - `DjangoIntegrationPipeline` - Saves items to Django models
   - `CleaningPipeline` - Basic HTML cleaning
   - `DeduplicationPipeline` - Checks for duplicate content

5. Create `scrapers/spiders/base.py`:
   - `BaseSpider` class with common functionality
   - Methods for date parsing, content cleaning
   - Error handling and logging

6. Add Django setup code to allow Scrapy to use Django models:
   ```python
   import os
   import django
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
   django.setup()
   ```

7. Update requirements to include:
   - scrapy>=2.11
   - scrapy-user-agents>=0.1.1
   - python-dateutil>=2.8

**Acceptance Criteria:**
- Scrapy project structure created
- `scrapy list` command works (shows no spiders yet)
- Django models accessible from Scrapy
- Pipelines can save to Django database
- Settings properly configured with rate limiting
- Base spider class provides reusable functionality

**Files to Create:**
- `scrapers/__init__.py`, `scrapers/scrapy.cfg`, `scrapers/settings.py`
- `scrapers/items.py`, `scrapers/pipelines.py`, `scrapers/middlewares.py`
- `scrapers/spiders/__init__.py`, `scrapers/spiders/base.py`
- `scrapers/tests/__init__.py`, `scrapers/tests/test_pipelines.py`

**Files to Modify:**
- `requirements/base.txt`

---

### TICKET-009: RSS Feed Spider Implementation
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-008

**Description:**
Implement a Scrapy spider for fetching content from RSS/Atom feeds.

**Requirements:**
1. In `scrapers/spiders/rss_spider.py`, create `RSSSpider`:
   - Inherit from `BaseSpider`
   - Accept source_id as argument
   - Fetch Source from database using source_id
   - Use feedparser library to parse RSS/Atom feeds
   - Extract: title, link, description, published date, author
   - Yield ContentItem for each entry
   - Handle various RSS/Atom formats
   - Handle missing or malformed dates
   - Log errors and update Source.mark_scrape_attempt()

2. Implement error handling:
   - Network errors
   - Invalid feed format
   - Missing required fields
   - Date parsing errors

3. Add support for:
   - RSS 2.0
   - Atom 1.0
   - Various date formats (RFC 822, ISO 8601)

4. Create Celery task in `apps/aggregation/tasks.py`:
   - `scrape_rss_source(source_id)` - Runs RSS spider for given source
   - Updates Source model after scraping
   - Handles exceptions and logs errors

5. Add unit tests for:
   - RSS parsing with sample feeds
   - Date parsing edge cases
   - Error handling

6. Update requirements to include:
   - feedparser>=6.0

**Acceptance Criteria:**
- RSS spider successfully parses RSS 2.0 and Atom 1.0 feeds
- Content saved to AggregatedContent model
- Source.last_checked_at updated after scraping
- Errors logged and Source.consecutive_failures incremented on failure
- Celery task can be called: `scrape_rss_source.delay(source_id)`
- Tests pass for various RSS formats
- Duplicate content not created (hash check works)

**Files to Create:**
- `scrapers/spiders/rss_spider.py`
- `apps/aggregation/tasks.py`
- `scrapers/tests/test_rss_spider.py`
- `scrapers/tests/fixtures/sample_rss.xml`

**Files to Modify:**
- `requirements/base.txt`

---

### TICKET-010: Content Processing Pipeline - Basic Cleaning
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-006, TICKET-007

**Description:**
Implement Celery tasks for processing raw aggregated content into cleaned, structured format.

**Requirements:**
1. Create `apps/content/services.py` with `ContentProcessor` class:
   - `clean_html(html_content)` - Strip HTML tags, keep text
   - `normalize_text(text)` - Remove extra whitespace, normalize
   - `extract_keywords(text, max_keywords=10)` - Simple keyword extraction
   - `calculate_word_count(text)` - Count words
   - `generate_summary(text, max_length=200)` - Extract first N chars as summary

2. Use libraries for HTML cleaning:
   - BeautifulSoup4 for HTML parsing
   - bleach for sanitization
   - re for text normalization

3. Create `apps/content/tasks.py` with:
   - `process_aggregated_content(aggregated_content_id)` - Main processing task
     - Fetch AggregatedContent by ID
     - Clean HTML from content_body
     - Normalize text
     - Extract keywords (simple frequency-based)
     - Calculate word count and reading time
     - Generate basic summary
     - Create ProcessedContent record
     - Mark AggregatedContent.is_processed = True
     - Handle errors and log

4. Create signal in `apps/aggregation/signals.py`:
   - Post-save signal on AggregatedContent
   - Automatically trigger processing task for new content

5. Add configuration in settings:
   - CONTENT_PROCESSING_ENABLED = True
   - CONTENT_PROCESSING_AUTO_TRIGGER = True

6. Create tests for:
   - HTML cleaning
   - Text normalization
   - Keyword extraction
   - End-to-end processing

7. Update requirements:
   - beautifulsoup4>=4.12
   - bleach>=6.0
   - lxml>=4.9

**Acceptance Criteria:**
- New AggregatedContent automatically triggers processing task
- HTML tags removed from content
- Keywords extracted (at least top 5)
- Word count and reading time calculated correctly
- ProcessedContent created with cleaned data
- is_processed flag set to True
- Tests pass for all processing functions
- Processing errors logged and don't crash

**Files to Create:**
- `apps/content/services.py`
- `apps/content/tasks.py`
- `apps/aggregation/signals.py`
- `apps/content/tests/test_services.py`
- `apps/content/tests/test_tasks.py`

**Files to Modify:**
- `apps/aggregation/apps.py` (register signals)
- `config/settings/base.py` (add processing config)
- `requirements/base.txt`

---

### TICKET-011: Celery Beat Scheduling for Scraping
**Priority:** HIGH | **Phase:** 1 | **Dependencies:** TICKET-009

**Description:**
Configure Celery Beat to automatically schedule scraping tasks based on Source.scrape_frequency.

**Requirements:**
1. Create `apps/aggregation/tasks.py` task:
   - `schedule_due_scraping()` - Periodic task that:
     - Queries Source.objects.due_for_scraping()
     - For each source, dispatches appropriate scraping task based on source_type
     - Logs scheduled tasks

2. In `config/settings/base.py`, add to CELERY_BEAT_SCHEDULE:
   ```python
   'schedule-scraping': {
       'task': 'apps.aggregation.tasks.schedule_due_scraping',
       'schedule': crontab(minute='*/15'),  # Every 15 minutes
   }
   ```

3. Create management command `apps/aggregation/management/commands/scrape_source.py`:
   - Manually trigger scraping for a specific source
   - Usage: `python manage.py scrape_source <source_id>`

4. Create management command `apps/aggregation/management/commands/add_test_sources.py`:
   - Add sample RSS feed sources for testing
   - Include feeds from known frugal living blogs

5. Add logging configuration for scraping tasks:
   - Separate log file for scraping: `logs/scraping.log`
   - Log level: INFO
   - Include timestamps, source info, success/failure

6. Create monitoring task in `apps/aggregation/tasks.py`:
   - `check_scraping_health()` - Runs daily
   - Identifies sources with high failure rates
   - Sends alert (log warning) for sources in 'error' status

**Acceptance Criteria:**
- Celery Beat schedules scraping every 15 minutes
- Only sources due for scraping are processed
- Manual scraping command works: `python manage.py scrape_source 1`
- Test sources can be added: `python manage.py add_test_sources`
- Scraping logs written to separate file
- Health check task identifies problematic sources
- No duplicate scraping tasks for same source

**Files to Create:**
- `apps/aggregation/management/__init__.py`
- `apps/aggregation/management/commands/__init__.py`
- `apps/aggregation/management/commands/scrape_source.py`
- `apps/aggregation/management/commands/add_test_sources.py`

**Files to Modify:**
- `apps/aggregation/tasks.py`
- `config/settings/base.py` (CELERY_BEAT_SCHEDULE, LOGGING)

---

### TICKET-012: Basic Frontend - Templates and Static Files
**Priority:** MEDIUM | **Phase:** 1 | **Dependencies:** TICKET-001

**Description:**
Set up basic frontend infrastructure with Django templates, static files, and HTMX integration.

**Requirements:**
1. Create `templates/base.html`:
   - HTML5 doctype
   - Include Bootstrap 5 CSS from CDN
   - Include HTMX from CDN (htmx.org)
   - Include Alpine.js from CDN (optional, for simple interactions)
   - Navigation bar with logo and menu
   - Main content block
   - Footer with copyright
   - Messages framework integration

2. Create `templates/home.html`:
   - Extends base.html
   - Hero section with platform description
   - Recent content section (placeholder)
   - Call-to-action for forum

3. Create `static/css/base.css`:
   - Custom CSS variables for colors
   - Typography styles
   - Utility classes
   - Responsive design helpers

4. Create `static/js/app.js`:
   - Initialize HTMX
   - Common JavaScript utilities
   - Form handling helpers

5. Configure static files in settings:
   - STATIC_URL = '/static/'
   - STATIC_ROOT = BASE_DIR / 'staticfiles'
   - STATICFILES_DIRS = [BASE_DIR / 'static']
   - Configure WhiteNoise for serving static files

6. Create `apps/core/views.py`:
   - `HomeView` - Renders home.html
   - `AboutView` - Renders about.html (create template)

7. Create `apps/core/urls.py`:
   - URL patterns for home and about pages

8. Update `config/urls.py`:
   - Include core.urls
   - Configure static/media file serving for development

9. Update requirements:
   - whitenoise>=6.5

**Acceptance Criteria:**
- Home page accessible at http://localhost:8000/
- Base template renders with navigation and footer
- Static CSS and JS files load correctly
- HTMX library loaded and functional
- Bootstrap styles applied
- Responsive design works on mobile
- About page accessible

**Files to Create:**
- `templates/base.html`, `templates/home.html`, `templates/about.html`
- `templates/components/navbar.html`, `templates/components/footer.html`
- `static/css/base.css`
- `static/js/app.js`
- `apps/core/views.py`, `apps/core/urls.py`

**Files to Modify:**
- `config/urls.py`
- `config/settings/base.py` (static files config)
- `requirements/base.txt`

---

### TICKET-013: Content Listing Views
**Priority:** MEDIUM | **Phase:** 1 | **Dependencies:** TICKET-012, TICKET-006

**Description:**
Create views and templates to display aggregated and processed content.

**Requirements:**
1. Create `apps/content/views.py`:
   - `ContentListView` (ListView):
     - Display ProcessedContent ordered by published_at
     - Paginate by 20 items
     - Filter by date range (optional query params)
     - Filter by source (optional query param)

   - `ContentDetailView` (DetailView):
     - Display single ProcessedContent with full cleaned_body
     - Show source information
     - Show keywords and metadata
     - Link to original source URL

2. Create templates:
   - `apps/content/templates/content/list.html`:
     - Extends base.html
     - Display content cards with title, summary, source, date
     - Pagination controls
     - Filter sidebar (by date, source)

   - `apps/content/templates/content/detail.html`:
     - Extends base.html
     - Full content display
     - Metadata sidebar
     - Related content section (placeholder)

3. Create `apps/content/urls.py`:
   - URL patterns for list and detail views
   - Use slug or ID for detail view

4. Update `config/urls.py` to include content.urls

5. Add HTMX enhancement:
   - Infinite scroll for content list
   - Load more button that fetches next page via HTMX

6. Create template tags in `apps/content/templatetags/content_tags.py`:
   - `truncate_words` - Truncate text to N words
   - `time_since` - Human-readable time since publication
   - `reading_time_badge` - Display reading time badge

**Acceptance Criteria:**
- Content list page shows all processed content
- Pagination works correctly
- Content detail page displays full content
- Filters work (by date, by source)
- HTMX infinite scroll loads more content
- Template tags work correctly
- Links to original sources work
- Responsive design on mobile

**Files to Create:**
- `apps/content/views.py`, `apps/content/urls.py`
- `apps/content/templates/content/list.html`
- `apps/content/templates/content/detail.html`
- `apps/content/templatetags/__init__.py`
- `apps/content/templatetags/content_tags.py`
- `apps/content/tests/test_views.py`

**Files to Modify:**
- `config/urls.py`
- `templates/base.html` (add link to content list in nav)

---

## PHASE 2: AI CONTENT GENERATION & DISTRIBUTION MVP

### TICKET-014: AI Integration - OpenAI/Anthropic SDK Setup
**Priority:** CRITICAL | **Phase:** 2 | **Dependencies:** TICKET-007

**Description:**
Set up integration with OpenAI and Anthropic APIs for AI content generation.

**Requirements:**
1. Create `apps/ai/` Django app for AI-related functionality

2. Create `apps/ai/clients.py` with client classes:
   - `BaseAIClient` abstract class with methods:
     - `generate_text(prompt, max_tokens, temperature)`
     - `count_tokens(text)`
     - `estimate_cost(tokens, model)`

   - `OpenAIClient` implementing BaseAIClient:
     - Initialize with API key from settings
     - Use openai Python SDK
     - Support GPT-4o and GPT-3.5-turbo models
     - Implement retry logic with exponential backoff
     - Handle rate limits and errors

   - `AnthropicClient` implementing BaseAIClient:
     - Initialize with API key from settings
     - Use anthropic Python SDK
     - Support Claude 3.5 Sonnet and Claude 3 Haiku
     - Implement retry logic
     - Handle rate limits and errors

3. Create `apps/ai/services.py` with:
   - `AIService` class that:
     - Selects appropriate client based on configuration
     - Provides unified interface for text generation
     - Logs all API calls (prompt, response, tokens, cost)
     - Implements caching for identical prompts (Redis)

4. Add settings in `config/settings/base.py`:
   - AI_PROVIDER = 'openai' or 'anthropic'
   - AI_MODEL = 'gpt-4o' or 'claude-3-5-sonnet'
   - AI_DEFAULT_MAX_TOKENS = 2000
   - AI_DEFAULT_TEMPERATURE = 0.7
   - AI_ENABLE_CACHING = True
   - AI_CACHE_TTL = 3600 (1 hour)

5. Create `apps/ai/models.py`:
   - `AIGenerationLog` model to track all AI API calls:
     - Fields: prompt, response, model_used, tokens_used, cost, created_at, task_type, success, error_message

6. Update requirements:
   - openai>=1.10
   - anthropic>=0.18

7. Create tests for:
   - Client initialization
   - Text generation (mocked)
   - Error handling
   - Caching behavior

**Acceptance Criteria:**
- OpenAI client successfully generates text
- Anthropic client successfully generates text
- API calls logged to database
- Caching reduces duplicate API calls
- Rate limit errors handled gracefully
- Cost tracking works correctly
- Tests pass with mocked API responses

**Files to Create:**
- `apps/ai/__init__.py`, `apps/ai/apps.py`, `apps/ai/models.py`, `apps/ai/admin.py`
- `apps/ai/clients.py`, `apps/ai/services.py`
- `apps/ai/migrations/0001_initial.py`
- `apps/ai/tests/__init__.py`, `apps/ai/tests/test_clients.py`, `apps/ai/tests/test_services.py`

**Files to Modify:**
- `config/settings/base.py`
- `.env.example` (add AI API keys)
- `requirements/base.txt`

---

### TICKET-015: AI Content Generation - Summary Articles
**Priority:** HIGH | **Phase:** 2 | **Dependencies:** TICKET-014, TICKET-006

**Description:**
Implement AI-powered generation of summary articles from processed content.

**Requirements:**
1. Update `apps/content/models.py` to add `GeneratedArticle` model:
   - Fields:
     - `title` (CharField, max_length=500)
     - `slug` (SlugField, unique=True, db_index=True)
     - `body` (TextField, markdown or rich text)
     - `excerpt` (TextField, max_length=500)
     - `source_references` (ManyToManyField to ProcessedContent)
     - `author_avatar` (ForeignKey to AIAvatar, null=True)
     - `generation_prompt` (TextField)
     - `model_used` (CharField, max_length=100)
     - `tokens_used` (IntegerField, default=0)
     - `generation_cost` (DecimalField, max_digits=10, decimal_places=6)
     - `generated_at` (DateTimeField, auto_now_add=True)
     - `status` (CharField, choices=['draft', 'review', 'published', 'archived'])
     - `published_at` (DateTimeField, null=True, blank=True)
     - `view_count` (IntegerField, default=0)
     - `comment_count` (IntegerField, default=0)
     - `meta_description` (CharField, max_length=160)
     - `tags` (ArrayField of CharField)

   - Methods:
     - `save()` - Auto-generate slug from title
     - `publish()` - Set status to published and set published_at
     - `__str__()` - Return title

2. Create `apps/content/services.py` with `ArticleGenerator` class:
   - `generate_daily_summary(date=None)` method:
     - Fetch ProcessedContent from last 24 hours
     - Group by topic/keywords
     - Create prompt for AI to generate summary article
     - Call AIService to generate content
     - Create GeneratedArticle with references
     - Return article instance

   - `generate_topic_article(topic, num_sources=5)` method:
     - Fetch relevant ProcessedContent by keyword/topic
     - Create detailed prompt for blog-style article
     - Generate article with AI
     - Create GeneratedArticle

3. Create prompt templates in `apps/content/prompts.py`:
   - `DAILY_SUMMARY_PROMPT` - Template for daily summaries
   - `TOPIC_ARTICLE_PROMPT` - Template for topic-based articles
   - Include instructions for: tone, structure, length, citation format

4. Create Celery task in `apps/content/tasks.py`:
   - `generate_daily_summary_task()` - Scheduled daily
   - `generate_topic_article_task(topic)` - On-demand

5. Add to CELERY_BEAT_SCHEDULE:
   ```python
   'generate-daily-summary': {
       'task': 'apps.content.tasks.generate_daily_summary_task',
       'schedule': crontab(hour=6, minute=0),  # 6 AM daily
   }
   ```

6. Create admin interface for GeneratedArticle with:
   - List view with filters (status, generated_at)
   - Detail view showing full content and metadata
   - Actions: publish, archive, regenerate

7. Create tests for article generation (with mocked AI)

**Acceptance Criteria:**
- Daily summary task generates article from recent content
- Generated articles saved with proper references
- Slug auto-generated from title
- AI costs tracked per article
- Admin can review and publish articles
- Tests pass with mocked AI responses
- Prompt templates produce quality output

**Files to Create:**
- `apps/content/prompts.py`
- `apps/content/tests/test_article_generation.py`

**Files to Modify:**
- `apps/content/models.py`
- `apps/content/services.py`
- `apps/content/tasks.py`
- `apps/content/admin.py`
- `config/settings/base.py` (CELERY_BEAT_SCHEDULE)

---

### TICKET-016: Generated Article Display Views
**Priority:** HIGH | **Phase:** 2 | **Dependencies:** TICKET-015

**Description:**
Create views and templates to display AI-generated articles.

**Requirements:**
1. Update `apps/content/views.py` to add:
   - `GeneratedArticleListView` (ListView):
     - Display published GeneratedArticle instances
     - Order by published_at descending
     - Paginate by 10 items
     - Filter by tags (optional)

   - `GeneratedArticleDetailView` (DetailView):
     - Display full article with markdown rendering
     - Show source references
     - Show generation metadata (model, date)
     - Increment view_count on each view
     - Show related articles

2. Create templates:
   - `apps/content/templates/content/generated_list.html`:
     - Card layout for articles
     - Show title, excerpt, tags, published date
     - Filter by tags sidebar

   - `apps/content/templates/content/generated_detail.html`:
     - Full article display with markdown rendering
     - Sidebar with metadata and source links
     - Related articles section
     - Social sharing buttons (placeholder)

3. Update `apps/content/urls.py`:
   - Add URL patterns for generated article views
   - Use slug for detail view

4. Install and configure markdown rendering:
   - Add markdown library to requirements
   - Create template filter for markdown rendering
   - Support code highlighting (optional)

5. Add SEO meta tags to generated article detail template:
   - Use meta_description field
   - Add Open Graph tags
   - Add Twitter Card tags

6. Create RSS feed for generated articles:
   - Use Django's syndication framework
   - Feed at `/feed/generated/`
   - Include last 20 published articles

**Acceptance Criteria:**
- Generated articles list page shows published articles
- Article detail page renders markdown correctly
- View count increments on each view
- Source references displayed with links
- RSS feed validates and shows articles
- SEO meta tags present in HTML
- Responsive design works

**Files to Create:**
- `apps/content/templates/content/generated_list.html`
- `apps/content/templates/content/generated_detail.html`
- `apps/content/feeds.py`
- `apps/content/tests/test_generated_views.py`

**Files to Modify:**
- `apps/content/views.py`
- `apps/content/urls.py`
- `apps/content/templatetags/content_tags.py` (add markdown filter)
- `requirements/base.txt` (add markdown>=3.5)
- `templates/base.html` (add link to generated articles in nav)

---

### TICKET-017: Newsletter Model and Generation
**Priority:** MEDIUM | **Phase:** 2 | **Dependencies:** TICKET-015

**Description:**
Implement newsletter model and AI-powered newsletter generation.

**Requirements:**
1. Update `apps/content/models.py` to add `Newsletter` model:
   - Fields:
     - `issue_number` (IntegerField, unique=True, db_index=True)
     - `issue_date` (DateField, db_index=True)
     - `subject` (CharField, max_length=255)
     - `html_body` (TextField)
     - `text_body` (TextField)
     - `included_articles` (ManyToManyField to GeneratedArticle)
     - `included_resources` (ManyToManyField to ProcessedContent)
     - `status` (CharField, choices=['draft', 'scheduled', 'sending', 'sent', 'failed'])
     - `scheduled_for` (DateTimeField, null=True, blank=True)
     - `sent_at` (DateTimeField, null=True, blank=True)
     - `recipient_count` (IntegerField, default=0)
     - `open_count` (IntegerField, default=0)
     - `click_count` (IntegerField, default=0)

   - Methods:
     - `__str__()` - Return issue number and date
     - `get_next_issue_number()` - Class method to get next issue number

2. Create `apps/content/services.py` with `NewsletterGenerator` class:
   - `generate_weekly_newsletter()` method:
     - Fetch top GeneratedArticles from past week
     - Fetch popular ProcessedContent
     - Create prompt for newsletter intro/outro
     - Generate HTML and text versions
     - Create Newsletter instance
     - Return newsletter

3. Create newsletter templates:
   - `apps/content/templates/email/newsletter_base.html`:
     - Responsive email HTML template
     - Header with logo
     - Content sections
     - Footer with unsubscribe link

   - `apps/content/templates/email/newsletter_text.txt`:
     - Plain text version

4. Create Celery task in `apps/content/tasks.py`:
   - `generate_weekly_newsletter_task()` - Scheduled weekly
   - Creates newsletter in 'draft' status for review

5. Add to CELERY_BEAT_SCHEDULE:
   ```python
   'generate-weekly-newsletter': {
       'task': 'apps.content.tasks.generate_weekly_newsletter_task',
       'schedule': crontab(day_of_week=1, hour=8, minute=0),  # Monday 8 AM
   }
   ```

6. Create admin interface for Newsletter:
   - Preview HTML and text versions
   - Actions: schedule, send test, send to all

7. Create tests for newsletter generation

**Acceptance Criteria:**
- Weekly newsletter task generates newsletter
- Newsletter includes recent articles and resources
- HTML and text versions generated
- Admin can preview and schedule newsletters
- Issue numbers auto-increment
- Tests pass

**Files to Create:**
- `apps/content/templates/email/newsletter_base.html`
- `apps/content/templates/email/newsletter_text.txt`
- `apps/content/tests/test_newsletter.py`

**Files to Modify:**
- `apps/content/models.py`
- `apps/content/services.py`
- `apps/content/tasks.py`
- `apps/content/admin.py`
- `config/settings/base.py` (CELERY_BEAT_SCHEDULE)

---

### TICKET-018: Email Subscription Management
**Priority:** MEDIUM | **Phase:** 2 | **Dependencies:** TICKET-017

**Description:**
Implement email subscription system for newsletter distribution.

**Requirements:**
1. Create `apps/subscribers/` Django app

2. Create `apps/subscribers/models.py` with:
   - `Subscriber` model:
     - Fields:
       - `email` (EmailField, unique=True, db_index=True)
       - `first_name` (CharField, max_length=100, blank=True)
       - `is_active` (BooleanField, default=True)
       - `subscribed_at` (DateTimeField, auto_now_add=True)
       - `unsubscribed_at` (DateTimeField, null=True, blank=True)
       - `confirmation_token` (CharField, max_length=64, unique=True)
       - `is_confirmed` (BooleanField, default=False)
       - `confirmed_at` (DateTimeField, null=True, blank=True)
       - `preferences` (JSONField, default=dict) # For future use

     - Methods:
       - `generate_confirmation_token()` - Generate unique token
       - `confirm()` - Mark as confirmed
       - `unsubscribe()` - Mark as unsubscribed
       - `__str__()` - Return email

3. Create `apps/subscribers/views.py`:
   - `SubscribeView` - Form to subscribe
   - `ConfirmSubscriptionView` - Confirm via token
   - `UnsubscribeView` - Unsubscribe via token
   - `SubscriptionSuccessView` - Success page

4. Create `apps/subscribers/forms.py`:
   - `SubscribeForm` with email and first_name fields
   - Email validation

5. Create templates:
   - `apps/subscribers/templates/subscribers/subscribe.html`
   - `apps/subscribers/templates/subscribers/confirm.html`
   - `apps/subscribers/templates/subscribers/unsubscribe.html`
   - `apps/subscribers/templates/subscribers/success.html`

6. Create `apps/subscribers/tasks.py`:
   - `send_confirmation_email(subscriber_id)` - Send double opt-in email
   - `send_newsletter_to_subscribers(newsletter_id)` - Send newsletter to all active subscribers

7. Configure email backend in settings:
   - Use console backend for development
   - Configure SMTP for production (via environment variables)

8. Create admin interface for Subscriber:
   - List view with filters (is_active, is_confirmed)
   - Actions: export emails, send test newsletter

9. Update Newsletter sending logic to use subscribers

**Acceptance Criteria:**
- Users can subscribe via form
- Confirmation email sent with unique token
- Double opt-in process works
- Users can unsubscribe via link
- Newsletter sent to all active, confirmed subscribers
- Admin can manage subscribers
- Tests pass for subscription flow

**Files to Create:**
- `apps/subscribers/__init__.py`, `apps/subscribers/apps.py`, `apps/subscribers/models.py`, `apps/subscribers/admin.py`
- `apps/subscribers/views.py`, `apps/subscribers/forms.py`, `apps/subscribers/urls.py`, `apps/subscribers/tasks.py`
- `apps/subscribers/templates/subscribers/subscribe.html`
- `apps/subscribers/templates/subscribers/confirm.html`
- `apps/subscribers/templates/subscribers/unsubscribe.html`
- `apps/subscribers/templates/subscribers/success.html`
- `apps/subscribers/templates/email/confirmation.html`
- `apps/subscribers/migrations/0001_initial.py`
- `apps/subscribers/tests/__init__.py`, `apps/subscribers/tests/test_models.py`, `apps/subscribers/tests/test_views.py`

**Files to Modify:**
- `config/urls.py` (include subscribers.urls)
- `config/settings/base.py` (email configuration)
- `templates/base.html` (add newsletter signup link)

---

## PHASE 3: COMMUNITY FORUM MVP

### TICKET-019: Users App - User Profile Model
**Priority:** HIGH | **Phase:** 3 | **Dependencies:** TICKET-001

**Description:**
Create users app with extended user profile functionality.

**Requirements:**
1. Create `apps/users/` Django app

2. Create `apps/users/models.py` with:
   - `UserProfile` model (OneToOne with Django User):
     - Fields:
       - `user` (OneToOneField to User, on_delete=CASCADE)
       - `bio` (TextField, max_length=500, blank=True)
       - `avatar` (ImageField, upload_to='avatars/', null=True, blank=True)
       - `location` (CharField, max_length=100, blank=True)
       - `website` (URLField, blank=True)
       - `forum_post_count` (IntegerField, default=0)
       - `forum_reputation` (IntegerField, default=0)
       - `interests` (ArrayField of CharField, default=list, blank=True)
       - `email_notifications` (BooleanField, default=True)
       - `created_at` (DateTimeField, auto_now_add=True)

     - Methods:
       - `__str__()` - Return username
       - `get_avatar_url()` - Return avatar URL or default

3. Create signal in `apps/users/signals.py`:
   - Post-save signal on User model
   - Automatically create UserProfile for new users

4. Create `apps/users/forms.py`:
   - `UserRegistrationForm` - Extends UserCreationForm
   - `UserProfileForm` - For editing profile
   - `UserSettingsForm` - For account settings

5. Create `apps/users/views.py`:
   - `RegisterView` - User registration
   - `ProfileView` - View user profile (own or others)
   - `ProfileEditView` - Edit own profile
   - `SettingsView` - Account settings

6. Create templates:
   - `apps/users/templates/users/register.html`
   - `apps/users/templates/users/login.html`
   - `apps/users/templates/users/profile.html`
   - `apps/users/templates/users/profile_edit.html`
   - `apps/users/templates/users/settings.html`

7. Create `apps/users/urls.py` with URL patterns

8. Configure authentication settings:
   - LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
   - Password validators

9. Create admin interface for UserProfile

10. Update requirements:
    - Pillow>=10.0 (for image handling)

**Acceptance Criteria:**
- Users can register with email and password
- UserProfile automatically created on registration
- Users can login and logout
- Users can view and edit their profiles
- Avatar upload works
- Email notifications setting saved
- Admin can manage user profiles
- Tests pass for registration and profile

**Files to Create:**
- `apps/users/__init__.py`, `apps/users/apps.py`, `apps/users/models.py`, `apps/users/admin.py`
- `apps/users/views.py`, `apps/users/forms.py`, `apps/users/urls.py`, `apps/users/signals.py`
- `apps/users/templates/users/register.html`, `apps/users/templates/users/login.html`
- `apps/users/templates/users/profile.html`, `apps/users/templates/users/profile_edit.html`
- `apps/users/templates/users/settings.html`
- `apps/users/migrations/0001_initial.py`
- `apps/users/tests/__init__.py`, `apps/users/tests/test_models.py`, `apps/users/tests/test_views.py`

**Files to Modify:**
- `apps/users/apps.py` (register signals)
- `config/urls.py` (include users.urls)
- `config/settings/base.py` (auth settings, media files)
- `requirements/base.txt`
- `templates/base.html` (add login/register links)

---

### TICKET-020: Forum App - Category and Topic Models
**Priority:** HIGH | **Phase:** 3 | **Dependencies:** TICKET-019

**Description:**
Create forum app with category and topic models for discussion threads.

**Requirements:**
1. Create `apps/forum/` Django app

2. Create `apps/forum/models.py` with:
   - `ForumCategory` model:
     - Fields:
       - `name` (CharField, max_length=100, unique=True)
       - `slug` (SlugField, unique=True, db_index=True)
       - `description` (TextField, max_length=500)
       - `order` (IntegerField, default=0) # For sorting
       - `is_active` (BooleanField, default=True)
       - `topic_count` (IntegerField, default=0)
       - `post_count` (IntegerField, default=0)
       - `created_at` (DateTimeField, auto_now_add=True)

     - Methods:
       - `save()` - Auto-generate slug
       - `update_counts()` - Update topic and post counts
       - `__str__()` - Return name

   - `ForumTopic` model:
     - Fields:
       - `category` (ForeignKey to ForumCategory, on_delete=CASCADE, related_name='topics')
       - `title` (CharField, max_length=255)
       - `slug` (SlugField, max_length=300, db_index=True)
       - `creator` (ForeignKey to User, on_delete=CASCADE, related_name='forum_topics')
       - `is_pinned` (BooleanField, default=False, db_index=True)
       - `is_locked` (BooleanField, default=False)
       - `view_count` (IntegerField, default=0)
       - `post_count` (IntegerField, default=0)
       - `created_at` (DateTimeField, auto_now_add=True, db_index=True)
       - `updated_at` (DateTimeField, auto_now=True)
       - `last_post_at` (DateTimeField, null=True, blank=True, db_index=True)
       - `last_post_by` (ForeignKey to User, null=True, on_delete=SET_NULL, related_name='+')

     - Methods:
       - `save()` - Auto-generate slug
       - `update_last_post()` - Update last_post_at and last_post_by
       - `increment_view_count()` - Increment views
       - `__str__()` - Return title

     - Meta:
       - `ordering = ['-is_pinned', '-last_post_at']`
       - Composite index on (category, is_pinned, last_post_at)

3. Create `apps/forum/managers.py`:
   - `ForumTopicManager` with methods:
     - `active()` - Return non-locked topics
     - `pinned()` - Return pinned topics
     - `recent()` - Return recently active topics

4. Create admin interface for ForumCategory and ForumTopic

5. Create migrations and apply them

6. Create tests for models

**Acceptance Criteria:**
- ForumCategory model created with all fields
- ForumTopic model created with all fields
- Slugs auto-generated from names/titles
- Counts update correctly
- Admin interface functional
- Tests pass
- Migrations apply successfully

**Files to Create:**
- `apps/forum/__init__.py`, `apps/forum/apps.py`, `apps/forum/models.py`, `apps/forum/admin.py`, `apps/forum/managers.py`
- `apps/forum/migrations/0001_initial.py`
- `apps/forum/tests/__init__.py`, `apps/forum/tests/test_models.py`, `apps/forum/tests/factories.py`

---

### TICKET-021: Forum App - Post Model and Moderation
**Priority:** HIGH | **Phase:** 3 | **Dependencies:** TICKET-020

**Description:**
Implement forum post model with moderation status tracking.

**Requirements:**
1. Update `apps/forum/models.py` to add `ForumPost` model:
   - Fields:
     - `topic` (ForeignKey to ForumTopic, on_delete=CASCADE, related_name='posts')
     - `author` (ForeignKey to User, on_delete=CASCADE, related_name='forum_posts')
     - `content` (TextField, max_length=10000)
     - `is_first_post` (BooleanField, default=False, db_index=True) # Topic starter
     - `created_at` (DateTimeField, auto_now_add=True, db_index=True)
     - `updated_at` (DateTimeField, auto_now=True)
     - `edited_at` (DateTimeField, null=True, blank=True)
     - `edited_by` (ForeignKey to User, null=True, on_delete=SET_NULL, related_name='+')
     - `moderation_status` (CharField, choices=['pending', 'approved', 'rejected', 'flagged_ai', 'flagged_user'], default='approved', db_index=True)
     - `moderation_details` (JSONField, default=dict, blank=True)
     - `is_deleted` (BooleanField, default=False)

   - Methods:
     - `mark_as_edited(editor)` - Update edited_at and edited_by
     - `soft_delete()` - Mark as deleted
     - `__str__()` - Return truncated content

   - Meta:
     - `ordering = ['created_at']`
     - Composite index on (topic, created_at)

2. Create signal in `apps/forum/signals.py`:
   - Post-save signal on ForumPost:
     - Update ForumTopic.post_count
     - Update ForumTopic.last_post_at and last_post_by
     - Update ForumCategory counts
     - Update UserProfile.forum_post_count
     - Trigger moderation task (if enabled)

3. Create `apps/forum/managers.py` with `ForumPostManager`:
   - `approved()` - Return only approved posts
   - `visible()` - Return approved and not deleted posts
   - `pending_moderation()` - Return posts needing review

4. Update admin interface to include ForumPost

5. Create tests for post model and signals

**Acceptance Criteria:**
- ForumPost model created with all fields
- Post creation updates topic and category counts
- Post creation updates user profile post count
- Moderation status tracked correctly
- Soft delete works
- Edit tracking works
- Tests pass

**Files to Create:**
- `apps/forum/signals.py`
- `apps/forum/tests/test_posts.py`

**Files to Modify:**
- `apps/forum/models.py`
- `apps/forum/managers.py`
- `apps/forum/admin.py`
- `apps/forum/apps.py` (register signals)

---

### TICKET-022: Forum Views - Category and Topic Listing
**Priority:** HIGH | **Phase:** 3 | **Dependencies:** TICKET-021

**Description:**
Create views and templates for displaying forum categories and topics.

**Requirements:**
1. Create `apps/forum/views.py`:
   - `ForumIndexView` (TemplateView):
     - Display all active categories
     - Show topic count and post count per category
     - Show latest post info per category

   - `CategoryDetailView` (ListView):
     - Display topics in a category
     - Paginate by 25 topics
     - Show pinned topics at top
     - Show topic stats (posts, views, last post)

   - `TopicDetailView` (DetailView):
     - Display topic with all posts
     - Paginate posts by 20 per page
     - Increment view count
     - Show reply form (if authenticated)

2. Create templates:
   - `apps/forum/templates/forum/index.html`:
     - List all categories
     - Show stats for each category
     - Recent activity section

   - `apps/forum/templates/forum/category_detail.html`:
     - List topics in category
     - Filter/sort options (recent, popular, unanswered)
     - "New Topic" button

   - `apps/forum/templates/forum/topic_detail.html`:
     - Display all posts in topic
     - Show author info sidebar for each post
     - Reply form at bottom
     - Edit/delete buttons (for own posts)

3. Create `apps/forum/urls.py` with URL patterns:
   - `/forum/` - Forum index
   - `/forum/<category_slug>/` - Category detail
   - `/forum/<category_slug>/<topic_slug>/` - Topic detail

4. Add HTMX enhancements:
   - Load more posts without page reload
   - Inline post editing
   - Quick reply form

5. Create template tags in `apps/forum/templatetags/forum_tags.py`:
   - `user_can_edit_post` - Check if user can edit post
   - `user_can_delete_post` - Check if user can delete post
   - `format_post_content` - Format markdown/BBCode

6. Create tests for views

**Acceptance Criteria:**
- Forum index shows all categories
- Category detail shows topics with pagination
- Topic detail shows posts with pagination
- View count increments on topic view
- HTMX enhancements work
- Template tags work correctly
- Tests pass

**Files to Create:**
- `apps/forum/views.py`, `apps/forum/urls.py`
- `apps/forum/templates/forum/index.html`
- `apps/forum/templates/forum/category_detail.html`
- `apps/forum/templates/forum/topic_detail.html`
- `apps/forum/templatetags/__init__.py`
- `apps/forum/templatetags/forum_tags.py`
- `apps/forum/tests/test_views.py`

**Files to Modify:**
- `config/urls.py` (include forum.urls)
- `templates/base.html` (add forum link in nav)

---

### TICKET-023: Forum Views - Topic and Post Creation
**Priority:** HIGH | **Phase:** 3 | **Dependencies:** TICKET-022

**Description:**
Implement views and forms for creating topics and posts.

**Requirements:**
1. Create `apps/forum/forms.py`:
   - `TopicCreateForm`:
     - Fields: title, content (for first post)
     - Validation: title length, content length
     - Clean methods for spam detection

   - `PostCreateForm`:
     - Fields: content
     - Validation: content length, rate limiting

   - `PostEditForm`:
     - Fields: content
     - Similar validation to PostCreateForm

2. Update `apps/forum/views.py` to add:
   - `TopicCreateView` (CreateView):
     - Require authentication
     - Accept category_slug in URL
     - Create both Topic and first Post
     - Redirect to new topic

   - `PostCreateView` (CreateView):
     - Require authentication
     - Accept topic_slug in URL
     - Create Post in topic
     - Update topic last_post info
     - Redirect to topic (last page)

   - `PostEditView` (UpdateView):
     - Require authentication
     - Check user owns post or is moderator
     - Update post content
     - Mark as edited
     - Redirect to topic

   - `PostDeleteView` (DeleteView):
     - Require authentication
     - Check user owns post or is moderator
     - Soft delete post
     - Redirect to topic

3. Add permission checks:
   - Create `apps/forum/permissions.py`:
     - `can_create_topic(user, category)` - Check if user can create topics
     - `can_reply_to_topic(user, topic)` - Check if topic is locked
     - `can_edit_post(user, post)` - Check ownership or moderator
     - `can_delete_post(user, post)` - Check ownership or moderator

4. Implement rate limiting:
   - Use Django cache to track post creation
   - Limit: 5 posts per 5 minutes per user
   - Show error message if limit exceeded

5. Create templates:
   - `apps/forum/templates/forum/topic_create.html`
   - `apps/forum/templates/forum/post_edit.html`

6. Add HTMX for inline reply form

7. Create tests for topic/post creation and editing

**Acceptance Criteria:**
- Authenticated users can create topics
- Authenticated users can reply to topics
- Users can edit their own posts
- Users can delete their own posts
- Moderators can edit/delete any post
- Rate limiting prevents spam
- Locked topics cannot receive replies
- Tests pass

**Files to Create:**
- `apps/forum/forms.py`
- `apps/forum/permissions.py`
- `apps/forum/templates/forum/topic_create.html`
- `apps/forum/templates/forum/post_edit.html`
- `apps/forum/tests/test_topic_creation.py`
- `apps/forum/tests/test_post_creation.py`

**Files to Modify:**
- `apps/forum/views.py`
- `apps/forum/urls.py`
- `apps/forum/templates/forum/category_detail.html` (add "New Topic" button)
- `apps/forum/templates/forum/topic_detail.html` (add reply form)

---

## PHASE 4: AI AVATARS & MODERATION

### TICKET-024: AI Avatar Model and Management
**Priority:** HIGH | **Phase:** 4 | **Dependencies:** TICKET-019, TICKET-014

**Description:**
Implement AI Avatar model for AI personas that participate in the forum.

**Requirements:**
1. Update `apps/users/models.py` to add `AIAvatar` model:
   - Fields:
     - `name` (CharField, max_length=100, unique=True)
     - `slug` (SlugField, unique=True, db_index=True)
     - `persona_description` (TextField) # Detailed persona for prompts
     - `short_bio` (CharField, max_length=200) # Public bio
     - `avatar` (ImageField, upload_to='ai_avatars/', null=True)
     - `generation_rules` (JSONField, default=dict) # Specific prompting rules
     - `expertise_areas` (ArrayField of CharField, default=list) # Topics of expertise
     - `is_active` (BooleanField, default=True, db_index=True)
     - `post_count` (IntegerField, default=0)
     - `created_at` (DateTimeField, auto_now_add=True)
     - `last_active_at` (DateTimeField, null=True, blank=True)

   - Methods:
     - `save()` - Auto-generate slug
     - `can_participate_in_topic(topic)` - Check if topic matches expertise
     - `get_participation_prompt(context)` - Generate prompt for participation
     - `__str__()` - Return name

2. Create `apps/users/services.py` with `AIAvatarService` class:
   - `get_avatar_for_topic(topic)` - Select appropriate avatar based on topic keywords
   - `should_avatar_participate(avatar, topic)` - Decide if avatar should participate
   - `generate_avatar_response(avatar, context, question=None)` - Generate AI response

3. Create admin interface for AIAvatar:
   - List view with filters (is_active, expertise_areas)
   - Form for editing persona and rules
   - Actions: activate, deactivate, test response

4. Create management command `apps/users/management/commands/create_default_avatars.py`:
   - Create 3-5 default AI avatars with different personas:
     - "Frugal Fred" - Budgeting expert
     - "Savvy Sarah" - Saving strategies expert
     - "Investment Ian" - Investment advice for beginners
     - "Deal Hunter Diana" - Deals and discounts expert
     - "Minimalist Mike" - Minimalism and decluttering

5. Update ForumPost model to support AI authors:
   - Change `author` field to allow null
   - Add `author_avatar` (ForeignKey to AIAvatar, null=True)
   - Add constraint: either author or author_avatar must be set

6. Create tests for AI avatar model and service

**Acceptance Criteria:**
- AIAvatar model created with all fields
- Default avatars can be created via management command
- Avatar selection logic works based on topic
- Admin interface functional
- ForumPost supports both human and AI authors
- Tests pass

**Files to Create:**
- `apps/users/services.py`
- `apps/users/management/commands/create_default_avatars.py`
- `apps/users/tests/test_ai_avatar.py`

**Files to Modify:**
- `apps/users/models.py`
- `apps/users/admin.py`
- `apps/forum/models.py` (update ForumPost)

---

### TICKET-025: AI Avatar Forum Participation - Topic Initiation
**Priority:** HIGH | **Phase:** 4 | **Dependencies:** TICKET-024, TICKET-015

**Description:**
Implement functionality for AI avatars to automatically initiate forum topics based on generated content.

**Requirements:**
1. Create `apps/forum/tasks.py` with Celery tasks:
   - `ai_avatar_initiate_topic_from_article(article_id, avatar_id=None)`:
     - Fetch GeneratedArticle by ID
     - Select appropriate AIAvatar (or use provided)
     - Generate discussion prompt based on article
     - Create ForumTopic with AI as creator
     - Create first ForumPost with discussion starter
     - Log activity

   - `schedule_ai_topic_initiation()`:
     - Periodic task (runs daily)
     - Find recent GeneratedArticles without forum topics
     - Select top 1-2 articles
     - Dispatch topic initiation tasks

2. Create prompt templates in `apps/forum/prompts.py`:
   - `TOPIC_INITIATION_PROMPT`:
     - Template for generating discussion starter
     - Include article summary, key points
     - Ask engaging question to community
     - Maintain avatar persona

3. Update `apps/forum/services.py` with:
   - `ForumAIService` class:
     - `create_topic_from_article(article, avatar)` - Create topic and first post
     - `generate_discussion_starter(article, avatar)` - Generate engaging post

4. Add to CELERY_BEAT_SCHEDULE:
   ```python
   'ai-initiate-topics': {
       'task': 'apps.forum.tasks.schedule_ai_topic_initiation',
       'schedule': crontab(hour=10, minute=0),  # 10 AM daily
   }
   ```

5. Add configuration in settings:
   - AI_FORUM_PARTICIPATION_ENABLED = True
   - AI_TOPIC_INITIATION_ENABLED = True
   - AI_MAX_TOPICS_PER_DAY = 2

6. Update forum templates to clearly label AI-initiated topics:
   - Add "AI Discussion" badge
   - Show avatar icon and name
   - Add disclaimer about AI participation

7. Create tests for topic initiation

**Acceptance Criteria:**
- AI avatars can create forum topics
- Topics based on generated articles
- Discussion starters are engaging and on-topic
- AI authorship clearly labeled
- Scheduled task creates topics daily
- Configuration settings respected
- Tests pass

**Files to Create:**
- `apps/forum/tasks.py`
- `apps/forum/prompts.py`
- `apps/forum/services.py`
- `apps/forum/tests/test_ai_participation.py`

**Files to Modify:**
- `config/settings/base.py` (CELERY_BEAT_SCHEDULE, AI config)
- `apps/forum/templates/forum/category_detail.html` (AI topic badges)
- `apps/forum/templates/forum/topic_detail.html` (AI author display)

---

### TICKET-026: AI Avatar Forum Participation - Q&A Responses
**Priority:** HIGH | **Phase:** 4 | **Dependencies:** TICKET-025

**Description:**
Implement AI avatar responses to user mentions and questions in forum.

**Requirements:**
1. Update `apps/forum/tasks.py` to add:
   - `ai_avatar_respond_to_mention(post_id, avatar_id)`:
     - Fetch ForumPost by ID
     - Extract question/context from post
     - Fetch relevant ProcessedContent for context
     - Generate AI response using avatar persona
     - Create ForumPost as reply
     - Log activity

   - `detect_avatar_mentions()`:
     - Periodic task (runs every 30 minutes)
     - Find recent posts mentioning AI avatars (@AvatarName)
     - Dispatch response tasks for each mention

2. Create `apps/forum/utils.py` with:
   - `extract_mentions(text)` - Extract @mentions from post content
   - `get_mentioned_avatars(post)` - Get AIAvatar instances mentioned
   - `get_conversation_context(post, num_posts=5)` - Get recent posts in thread

3. Update prompt templates in `apps/forum/prompts.py`:
   - `QA_RESPONSE_PROMPT`:
     - Template for answering questions
     - Include conversation context
     - Include relevant knowledge from ProcessedContent
     - Maintain avatar persona
     - Keep response concise and helpful

4. Update `apps/forum/services.py`:
   - `ForumAIService.generate_response_to_mention(post, avatar)`:
     - Get conversation context
     - Search for relevant content
     - Generate response
     - Return response text

5. Create signal in `apps/forum/signals.py`:
   - Post-save signal on ForumPost
   - Detect mentions in new posts
   - Trigger AI response tasks asynchronously

6. Add to CELERY_BEAT_SCHEDULE:
   ```python
   'ai-detect-mentions': {
       'task': 'apps/forum.tasks.detect_avatar_mentions',
       'schedule': crontab(minute='*/30'),  # Every 30 minutes
   }
   ```

7. Add rate limiting for AI responses:
   - Max 1 response per avatar per topic per hour
   - Prevent AI from dominating conversations

8. Create tests for mention detection and responses

**Acceptance Criteria:**
- AI avatars respond when mentioned
- Responses are contextually relevant
- Conversation context included in prompts
- Rate limiting prevents spam
- AI responses clearly labeled
- Tests pass

**Files to Create:**
- `apps/forum/utils.py`
- `apps/forum/tests/test_ai_mentions.py`

**Files to Modify:**
- `apps/forum/tasks.py`
- `apps/forum/prompts.py`
- `apps/forum/services.py`
- `apps/forum/signals.py`
- `config/settings/base.py` (CELERY_BEAT_SCHEDULE)

---

### TICKET-027: Content Moderation - Keyword and Rule-Based Filtering
**Priority:** HIGH | **Phase:** 4 | **Dependencies:** TICKET-021

**Description:**
Implement first layer of content moderation using keyword and rule-based filtering.

**Requirements:**
1. Create `apps/moderation/` Django app

2. Create `apps/moderation/models.py` with:
   - `ModerationRule` model:
     - Fields:
       - `name` (CharField, max_length=100)
       - `rule_type` (CharField, choices=['keyword', 'regex', 'length', 'link_count'])
       - `pattern` (TextField) # Keyword or regex pattern
       - `severity` (CharField, choices=['low', 'medium', 'high', 'critical'])
       - `action` (CharField, choices=['flag', 'reject', 'auto_approve'])
       - `is_active` (BooleanField, default=True)
       - `created_at` (DateTimeField, auto_now_add=True)

     - Methods:
       - `check_content(text)` - Check if content matches rule
       - `__str__()` - Return name

   - `ModerationLog` model:
     - Fields:
       - `content_type` (ForeignKey to ContentType)
       - `object_id` (PositiveIntegerField)
       - `content_object` (GenericForeignKey)
       - `action` (CharField, choices=['flagged_ai', 'flagged_keyword', 'approved_auto', 'approved_human', 'rejected_auto', 'rejected_human'])
       - `moderator_user` (ForeignKey to User, null=True)
       - `reason` (TextField)
       - `details` (JSONField, default=dict) # Scores, matched rules, etc.
       - `timestamp` (DateTimeField, auto_now_add=True)

     - Methods:
       - `__str__()` - Return action and timestamp

3. Create `apps/moderation/services.py` with:
   - `ModerationService` class:
     - `check_content(text, content_type='post')` - Run all active rules
     - `apply_keyword_rules(text)` - Check keyword rules
     - `apply_regex_rules(text)` - Check regex rules
     - `apply_length_rules(text)` - Check length constraints
     - `apply_link_rules(text)` - Check link count
     - `determine_action(matched_rules)` - Decide action based on severity
     - `log_moderation(content_object, action, reason, details)` - Create log entry

4. Create default moderation rules via management command:
   - `apps/moderation/management/commands/create_default_rules.py`:
     - Hate speech keywords (critical severity, reject)
     - Spam patterns (high severity, flag)
     - Excessive links (medium severity, flag)
     - Very short posts (low severity, flag)

5. Create `apps/moderation/tasks.py`:
   - `moderate_content(content_type, object_id)` - Celery task for moderation
   - Runs keyword/rule checks
   - Updates moderation_status on content
   - Creates ModerationLog entry

6. Update ForumPost save signal to trigger moderation:
   - Call moderate_content task asynchronously

7. Create admin interface for ModerationRule and ModerationLog

8. Create tests for moderation rules and service

**Acceptance Criteria:**
- ModerationRule model created
- ModerationLog model created
- Keyword rules detect prohibited content
- Regex rules work correctly
- Length and link rules work
- Default rules created via command
- Moderation triggered on post creation
- Admin can manage rules
- Tests pass

**Files to Create:**
- `apps/moderation/__init__.py`, `apps/moderation/apps.py`, `apps/moderation/models.py`, `apps/moderation/admin.py`
- `apps/moderation/services.py`, `apps/moderation/tasks.py`
- `apps/moderation/management/commands/create_default_rules.py`
- `apps/moderation/migrations/0001_initial.py`
- `apps/moderation/tests/__init__.py`, `apps/moderation/tests/test_services.py`

**Files to Modify:**
- `apps/forum/signals.py` (trigger moderation on post save)
- `config/settings/base.py` (add moderation config)

---

### TICKET-028: Content Moderation - AI-Powered Analysis
**Priority:** HIGH | **Phase:** 4 | **Dependencies:** TICKET-027, TICKET-014

**Description:**
Implement AI-powered content moderation for toxicity and spam detection.

**Requirements:**
1. Update `apps/moderation/services.py` to add:
   - `AIModeration` class:
     - `analyze_toxicity(text)` - Use LLM to detect toxicity
     - `analyze_spam(text)` - Use LLM to detect spam
     - `analyze_sentiment(text)` - Analyze sentiment
     - `get_moderation_scores(text)` - Get all scores
     - `should_flag_content(scores)` - Decide based on thresholds

2. Create moderation prompts in `apps/moderation/prompts.py`:
   - `TOXICITY_ANALYSIS_PROMPT`:
     - Analyze text for toxicity, hate speech, harassment
     - Return JSON with scores (0.0-1.0) for each category

   - `SPAM_ANALYSIS_PROMPT`:
     - Analyze text for spam indicators
     - Return JSON with spam score and reasoning

3. Update `apps/moderation/tasks.py`:
   - Modify `moderate_content` task to include AI analysis:
     - First run keyword/rule checks
     - If passes, run AI analysis
     - Combine results to determine final action
     - Log all scores and decisions

4. Add configuration in settings:
   - MODERATION_AI_ENABLED = True
   - MODERATION_TOXICITY_THRESHOLD = 0.7
   - MODERATION_SPAM_THRESHOLD = 0.8
   - MODERATION_AUTO_REJECT_THRESHOLD = 0.9

5. Create `apps/moderation/views.py`:
   - `ModerationQueueView` - List flagged content for review
   - `ModerationReviewView` - Review and take action on flagged content
   - Require moderator permissions

6. Create templates:
   - `apps/moderation/templates/moderation/queue.html`:
     - List flagged posts
     - Show AI scores and matched rules
     - Actions: approve, reject, delete

   - `apps/moderation/templates/moderation/review_detail.html`:
     - Full content display
     - Moderation history
     - Action form

7. Create `apps/moderation/urls.py` with URL patterns

8. Add user group and permissions:
   - Create "Moderators" group
   - Assign moderation permissions

9. Create tests for AI moderation

**Acceptance Criteria:**
- AI toxicity analysis works
- AI spam detection works
- Scores logged in ModerationLog
- Thresholds determine auto-actions
- Moderators can review flagged content
- Moderators can approve/reject content
- Tests pass with mocked AI

**Files to Create:**
- `apps/moderation/prompts.py`
- `apps/moderation/views.py`, `apps/moderation/urls.py`
- `apps/moderation/templates/moderation/queue.html`
- `apps/moderation/templates/moderation/review_detail.html`
- `apps/moderation/tests/test_ai_moderation.py`

**Files to Modify:**
- `apps/moderation/services.py`
- `apps/moderation/tasks.py`
- `config/settings/base.py` (moderation thresholds)
- `config/urls.py` (include moderation.urls)

---

### TICKET-029: Testing and Documentation
**Priority:** MEDIUM | **Phase:** 4 | **Dependencies:** All previous tickets

**Description:**
Comprehensive testing suite and documentation for the platform.

**Requirements:**
1. Create comprehensive test suite:
   - Ensure all apps have test coverage >80%
   - Create integration tests for key workflows:
     - Content aggregation → processing → display
     - AI article generation → publication
     - User registration → forum participation
     - AI avatar participation
     - Content moderation flow

2. Create `pytest.ini` configuration:
   - Configure test database
   - Set up coverage reporting
   - Configure test markers

3. Create factory classes for all models:
   - Use factory_boy
   - Create realistic test data
   - Support related objects

4. Update `README.md` with:
   - Project overview
   - Architecture diagram
   - Setup instructions (local and Docker)
   - Environment variables documentation
   - Running tests
   - Deployment guide

5. Create `docs/` directory with:
   - `docs/ARCHITECTURE.md` - System architecture
   - `docs/API.md` - Internal API documentation
   - `docs/DEPLOYMENT.md` - Deployment guide
   - `docs/DEVELOPMENT.md` - Development guide
   - `docs/MODERATION.md` - Moderation guidelines

6. Add docstrings to all:
   - Models (class and field descriptions)
   - Views (purpose and parameters)
   - Services (method descriptions)
   - Tasks (what they do and when they run)

7. Create management command for running checks:
   - `python manage.py system_check` - Check system health
   - Verify database connectivity
   - Verify Redis connectivity
   - Verify Celery workers
   - Verify AI API keys
   - Check for pending migrations

**Acceptance Criteria:**
- Test coverage >80% for all apps
- All integration tests pass
- README comprehensive and accurate
- Documentation complete
- All code has docstrings
- System check command works
- CI/CD pipeline configured (if applicable)

**Files to Create:**
- `pytest.ini`
- `docs/ARCHITECTURE.md`, `docs/API.md`, `docs/DEPLOYMENT.md`, `docs/DEVELOPMENT.md`, `docs/MODERATION.md`
- `apps/core/management/commands/system_check.py`
- Integration test files in each app

**Files to Modify:**
- `README.md`
- All model, view, service, and task files (add docstrings)

---

### TICKET-030: Production Deployment Configuration
**Priority:** MEDIUM | **Phase:** 4 | **Dependencies:** TICKET-029

**Description:**
Configure the application for production deployment with security and performance optimizations.

**Requirements:**
1. Update `config/settings/production.py`:
   - Set DEBUG = False
   - Configure ALLOWED_HOSTS from environment
   - Set secure cookie settings (SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE)
   - Configure SECURE_HSTS settings
   - Set up logging to file and external service (Sentry)
   - Configure static file serving with WhiteNoise
   - Set up database connection pooling

2. Create `docker-compose.prod.yml`:
   - Production-ready service configuration
   - Use gunicorn for Django
   - Use nginx as reverse proxy
   - Configure SSL/TLS certificates
   - Set resource limits
   - Configure health checks

3. Create `docker/nginx.conf`:
   - Reverse proxy configuration
   - Static file serving
   - SSL configuration
   - Security headers
   - Rate limiting

4. Create deployment scripts:
   - `scripts/deploy.sh` - Deployment script
   - `scripts/backup_db.sh` - Database backup
   - `scripts/restore_db.sh` - Database restore

5. Configure environment variables for production:
   - Update `.env.example` with production variables
   - Document all required variables

6. Set up monitoring:
   - Configure Sentry for error tracking
   - Set up application performance monitoring
   - Configure Celery monitoring with Flower

7. Create health check endpoints:
   - `/health/` - Basic health check
   - `/health/db/` - Database connectivity
   - `/health/redis/` - Redis connectivity
   - `/health/celery/` - Celery worker status

8. Security checklist:
   - Run `python manage.py check --deploy`
   - Fix all security warnings
   - Configure CORS if needed
   - Set up rate limiting
   - Configure CSP headers

**Acceptance Criteria:**
- Production settings configured correctly
- Docker Compose production setup works
- Nginx configuration correct
- Deployment scripts functional
- Health check endpoints work
- Security check passes
- Monitoring configured
- Documentation updated

**Files to Create:**
- `docker-compose.prod.yml`
- `docker/nginx.conf`
- `scripts/deploy.sh`, `scripts/backup_db.sh`, `scripts/restore_db.sh`
- `apps/core/views.py` (health check views)

**Files to Modify:**
- `config/settings/production.py`
- `config/urls.py` (add health check URLs)
- `.env.example`
- `docs/DEPLOYMENT.md`

---

## PHASE 5: ADVANCED FEATURES & ENHANCEMENTS

### TICKET-031: Automated Source Discovery and Vetting System
**Priority:** MEDIUM | **Phase:** 5 | **Dependencies:** TICKET-009, TICKET-010

**Description:**
Implement an automated system to discover new frugal living content sources, score their relevance and quality, and add vetted sources to the active scraping pool.

**Requirements:**

1. **Create SourceDiscovery Model:**
   - `apps/aggregation/models.py` - Add `SourceDiscovery` model
   - Fields:
     - `url` (URLField, unique=True, db_index=True)
     - `discovered_via` (CharField: 'search_api', 'link_analysis', 'sitemap', 'manual')
     - `discovered_at` (DateTimeField, auto_now_add=True, db_index=True)
     - `relevance_score` (FloatField, default=0.0, help_text="0.0-1.0 relevance score")
     - `quality_score` (FloatField, default=0.0, help_text="0.0-1.0 quality score")
     - `has_rss_feed` (BooleanField, default=False)
     - `rss_feed_url` (URLField, null=True, blank=True)
     - `has_api` (BooleanField, default=False)
     - `api_endpoint` (URLField, null=True, blank=True)
     - `content_sample` (TextField, blank=True, help_text="Sample content for analysis")
     - `metadata` (JSONField, default=dict, help_text="Additional discovery metadata")
     - `vetting_status` (CharField: 'pending', 'approved', 'rejected', 'needs_review', default='pending', db_index=True)
     - `vetting_notes` (TextField, blank=True)
     - `vetted_by` (ForeignKey to User, null=True, blank=True)
     - `vetted_at` (DateTimeField, null=True, blank=True)
     - `promoted_to_source` (BooleanField, default=False, db_index=True)
     - `promoted_source` (ForeignKey to Source, null=True, blank=True)
   - Methods:
     - `calculate_relevance_score()` - Calculate relevance based on keywords, geography
     - `calculate_quality_score()` - Calculate quality based on content depth, update frequency
     - `check_for_rss_feed()` - Attempt to discover RSS feed
     - `check_for_api()` - Check for API availability
     - `promote_to_source()` - Create Source from approved discovery

2. **Create Discovery Spiders:**
   - `scrapers/buxmax_scraper/spiders/discovery_spider.py`
   - `SourceDiscoverySpider` class:
     - Crawl known aggregators (e.g., personal finance blog directories)
     - Analyze outgoing links from high-quality existing sources
     - Parse sitemap.xml files from discovered domains
     - Extract potential source URLs and metadata
   - `SearchAPIDiscoverySpider` class:
     - Integrate with Google Custom Search JSON API
     - Search for keywords: "frugal living blog", "personal finance Canada", "saving money tips USA"
     - Extract URLs from search results
     - Store API response metadata

3. **Create Discovery Service:**
   - `apps/aggregation/services/discovery_service.py`
   - `SourceDiscoveryService` class with methods:
     - `discover_from_existing_sources()` - Analyze links from current sources
     - `discover_from_search_api(query, region='US')` - Use search API
     - `discover_from_sitemap(domain)` - Parse sitemap.xml
     - `analyze_discovered_source(discovery)` - Run all checks and scoring
     - `check_rss_feed(url)` - Attempt to find and validate RSS feed
     - `extract_content_sample(url)` - Fetch sample content for analysis
     - `calculate_relevance(content_sample, metadata)` - Score relevance using keywords
     - `calculate_quality(content_sample, metadata)` - Score quality using heuristics
     - `auto_vet_source(discovery)` - Automatic vetting based on scores
     - `promote_approved_sources()` - Convert approved discoveries to active sources

4. **Create AI-Powered Vetting:**
   - `apps/aggregation/prompts.py` - Add `SOURCE_VETTING_PROMPT`
   - Prompt should analyze:
     - Content relevance to frugal living (US/Canada focus)
     - Content quality and depth
     - Update frequency indicators
     - Geographic relevance
     - Potential spam or low-quality indicators
   - Return JSON with scores and reasoning
   - Update `SourceDiscoveryService` to use AI vetting

5. **Create Discovery Tasks:**
   - `apps/aggregation/tasks.py` - Add discovery tasks:
     - `discover_sources_from_search(query, region='US')` - Search API discovery
     - `discover_sources_from_existing()` - Link analysis from current sources
     - `analyze_pending_discoveries()` - Process pending discoveries
     - `auto_vet_discoveries()` - Run automatic vetting on analyzed discoveries
     - `promote_approved_discoveries()` - Convert approved to active sources
   - Add to Celery Beat schedule:
     - Search discovery: Weekly
     - Link analysis: Daily
     - Analysis: Every 6 hours
     - Auto-vetting: Every 12 hours
     - Promotion: Daily

6. **Create Admin Interface:**
   - `apps/aggregation/admin.py` - Add `SourceDiscoveryAdmin`
   - List display: url, discovered_via, relevance_score, quality_score, vetting_status
   - List filters: vetting_status, discovered_via, has_rss_feed, promoted_to_source
   - Search fields: url, content_sample
   - Actions:
     - `approve_sources` - Bulk approve
     - `reject_sources` - Bulk reject
     - `analyze_sources` - Trigger analysis
     - `promote_to_active_sources` - Bulk promote

7. **Create Vetting Dashboard:**
   - `apps/aggregation/templates/aggregation/discovery_queue.html`
   - Display pending discoveries with scores
   - Show content samples
   - Provide approve/reject/needs_review buttons
   - Filter by score ranges, discovery method

**Acceptance Criteria:**
- SourceDiscovery model created with all fields
- Discovery spiders can find new sources via multiple methods
- AI-powered vetting analyzes content relevance and quality
- Automatic vetting approves high-scoring sources
- Admin can review and manually approve/reject discoveries
- Approved sources automatically promoted to active Source model
- Celery tasks run on schedule to continuously discover sources
- Dashboard shows pending discoveries for human review

**Files to Create:**
- `apps/aggregation/services/discovery_service.py`
- `scrapers/buxmax_scraper/spiders/discovery_spider.py`
- `apps/aggregation/templates/aggregation/discovery_queue.html`
- `apps/aggregation/views/discovery_views.py`

**Files to Modify:**
- `apps/aggregation/models.py` (add SourceDiscovery model)
- `apps/aggregation/tasks.py` (add discovery tasks)
- `apps/aggregation/admin.py` (add SourceDiscoveryAdmin)
- `apps/aggregation/prompts.py` (add SOURCE_VETTING_PROMPT)
- `config/settings/base.py` (add CELERY_BEAT_SCHEDULE entries, GOOGLE_SEARCH_API_KEY)
- `apps/aggregation/urls.py` (add discovery queue URL)

---

### TICKET-032: Advanced Scraping with JavaScript Rendering and Anti-Detection
**Priority:** MEDIUM | **Phase:** 5 | **Dependencies:** TICKET-008, TICKET-009

**Description:**
Enhance the scraping infrastructure to handle JavaScript-heavy websites using Playwright and implement anti-detection measures for reliable scraping of protected sources.

**Requirements:**

1. **Install Dependencies:**
   - Add to `requirements/base.txt`:
     - `playwright>=1.40.0`
     - `scrapy-playwright>=0.0.34`
     - `curl-cffi>=0.6.0` (for TLS fingerprint spoofing)
   - Create installation script: `scripts/install_playwright.sh`
   - Install Playwright browsers: `playwright install chromium`

2. **Configure Scrapy-Playwright Middleware:**
   - Update `scrapers/buxmax_scraper/settings.py`:
     - Add `DOWNLOAD_HANDLERS` for playwright
     - Add `TWISTED_REACTOR` = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
     - Configure `PLAYWRIGHT_BROWSER_TYPE` = 'chromium'
     - Configure `PLAYWRIGHT_LAUNCH_OPTIONS`:
       - `headless=True`
       - `args=['--disable-blink-features=AutomationControlled']`
     - Add `PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT` = 30000
     - Add `PLAYWRIGHT_CONTEXTS` with stealth settings

3. **Create Playwright-Enabled Base Spider:**
   - `scrapers/buxmax_scraper/spiders/base_playwright_spider.py`
   - `PlaywrightSpider` base class:
     - Configure playwright meta for requests
     - Implement wait strategies (wait_for_selector, wait_for_load_state)
     - Handle infinite scroll
     - Handle dynamic content loading
     - Screenshot capability for debugging
     - Methods:
       - `wait_for_element(selector, timeout=10000)`
       - `scroll_to_bottom(max_scrolls=10)`
       - `click_load_more_button(selector)`
       - `extract_after_js_render()`

4. **Create JavaScript-Heavy Site Spiders:**
   - `scrapers/buxmax_scraper/spiders/js_blog_spider.py`
   - `JavaScriptBlogSpider` class (inherits from PlaywrightSpider):
     - Handle single-page applications (SPAs)
     - Wait for content to load
     - Extract data after JavaScript execution
     - Handle lazy-loaded images and content
   - `scrapers/buxmax_scraper/spiders/js_forum_spider.py`
   - `JavaScriptForumSpider` class:
     - Handle infinite scroll forums
     - Click "Load More" buttons
     - Extract dynamically loaded posts

5. **Implement Anti-Detection Measures:**
   - `scrapers/buxmax_scraper/middlewares/stealth_middleware.py`
   - `StealthMiddleware` class:
     - Rotate user agents from realistic pool
     - Randomize request delays (1-5 seconds)
     - Rotate proxies (if configured)
     - Add realistic browser headers
     - Implement request fingerprint randomization
   - `scrapers/buxmax_scraper/middlewares/curl_cffi_middleware.py`
   - `CurlCffiMiddleware` class:
     - Use curl_cffi for TLS fingerprint spoofing
     - Mimic real browser TLS handshakes
     - Bypass basic TLS-based bot detection

6. **Create Retry and Error Handling:**
   - Update `scrapers/buxmax_scraper/middlewares/retry_middleware.py`
   - Enhanced retry logic for:
     - CAPTCHA detection (log and skip)
     - Rate limiting (exponential backoff)
     - Temporary blocks (longer delays)
     - JavaScript errors (retry with different settings)
   - Implement CAPTCHA detection:
     - Check for common CAPTCHA indicators in response
     - Log CAPTCHA encounters for manual review
     - Mark source as 'captcha_blocked' status

7. **Create Monitoring and Logging:**
   - `apps/aggregation/models.py` - Update Source model:
     - Add `requires_javascript` (BooleanField, default=False)
     - Add `uses_anti_detection` (BooleanField, default=False)
     - Add `captcha_encountered_count` (IntegerField, default=0)
     - Add `last_captcha_at` (DateTimeField, null=True)
     - Add `blocked_status` (CharField: 'active', 'rate_limited', 'captcha_blocked', 'ip_blocked')
   - Enhanced logging for:
     - JavaScript rendering time
     - Anti-detection measure effectiveness
     - CAPTCHA encounters
     - Block detection

8. **Create Configuration Management:**
   - `config/settings/base.py` - Add settings:
     - `PLAYWRIGHT_ENABLED` = True
     - `ANTI_DETECTION_ENABLED` = True
     - `PROXY_POOL` = [] (list of proxy URLs)
     - `USER_AGENT_POOL` = [] (list of realistic user agents)
     - `CAPTCHA_DETECTION_ENABLED` = True
   - `scrapers/buxmax_scraper/user_agents.py` - Pool of realistic user agents
   - `scrapers/buxmax_scraper/proxies.py` - Proxy rotation logic

9. **Create Admin Tools:**
   - Add admin actions to `SourceAdmin`:
     - `enable_javascript_rendering` - Mark sources as requiring JS
     - `enable_anti_detection` - Enable anti-detection for sources
     - `reset_block_status` - Reset blocked sources
     - `test_scrape_with_playwright` - Test scrape with Playwright

**Acceptance Criteria:**
- Playwright successfully integrated with Scrapy
- Spiders can scrape JavaScript-heavy websites
- Anti-detection middleware rotates user agents and adds realistic headers
- TLS fingerprint spoofing works with curl_cffi
- CAPTCHA detection logs encounters and pauses scraping
- Infinite scroll and dynamic content handled correctly
- Source model tracks JavaScript requirements and block status
- Admin can configure which sources use advanced features
- Monitoring shows JavaScript rendering performance
- Error handling gracefully manages blocks and CAPTCHAs

**Files to Create:**
- `scrapers/buxmax_scraper/spiders/base_playwright_spider.py`
- `scrapers/buxmax_scraper/spiders/js_blog_spider.py`
- `scrapers/buxmax_scraper/spiders/js_forum_spider.py`
- `scrapers/buxmax_scraper/middlewares/stealth_middleware.py`
- `scrapers/buxmax_scraper/middlewares/curl_cffi_middleware.py`
- `scrapers/buxmax_scraper/user_agents.py`
- `scrapers/buxmax_scraper/proxies.py`
- `scripts/install_playwright.sh`

**Files to Modify:**
- `scrapers/buxmax_scraper/settings.py` (add Playwright configuration)
- `scrapers/buxmax_scraper/middlewares/retry_middleware.py` (enhance retry logic)
- `apps/aggregation/models.py` (add JavaScript and blocking fields to Source)
- `apps/aggregation/admin.py` (add admin actions)
- `requirements/base.txt` (add playwright, scrapy-playwright, curl-cffi)
- `config/settings/base.py` (add Playwright settings)

---

### TICKET-033: Enhanced Newsletter Distribution with ESP Integration
**Priority:** MEDIUM | **Phase:** 5 | **Dependencies:** TICKET-017, TICKET-018

**Description:**
Enhance the newsletter distribution system with Email Service Provider (ESP) integration for improved deliverability, tracking, and subscriber management using SendGrid and Mailchimp APIs.

**Requirements:**

1. **Install ESP SDKs:**
   - Add to `requirements/base.txt`:
     - `sendgrid>=6.10.0`
     - `mailchimp-marketing>=3.0.80`
   - Add to `.env.example`:
     - `SENDGRID_API_KEY=`
     - `SENDGRID_FROM_EMAIL=`
     - `MAILCHIMP_API_KEY=`
     - `MAILCHIMP_SERVER_PREFIX=` (e.g., 'us1')
     - `MAILCHIMP_LIST_ID=`
     - `ESP_PROVIDER=sendgrid` (or 'mailchimp' or 'django')

2. **Create ESP Service Abstraction:**
   - `apps/content/services/esp_service.py`
   - `BaseESPService` abstract class with methods:
     - `send_email(to_email, subject, html_content, text_content, from_email=None)`
     - `send_bulk_emails(recipients, subject, html_content, text_content)`
     - `add_subscriber(email, first_name='', last_name='', tags=[])`
     - `remove_subscriber(email)`
     - `update_subscriber(email, **kwargs)`
     - `get_subscriber_status(email)`
     - `track_email_event(event_type, email, newsletter_id, metadata={})`

3. **Implement SendGrid Service:**
   - `apps/content/services/sendgrid_service.py`
   - `SendGridService` class (inherits from BaseESPService):
     - Initialize with API key from settings
     - Implement `send_email()` using SendGrid Mail API
     - Implement `send_bulk_emails()` with batch sending (max 1000 per batch)
     - Implement `add_subscriber()` using Marketing Campaigns API
     - Implement `remove_subscriber()` with suppression list
     - Implement subscriber management methods
     - Handle SendGrid-specific errors and rate limits
     - Add retry logic with exponential backoff

4. **Implement Mailchimp Service:**
   - `apps/content/services/mailchimp_service.py`
   - `MailchimpService` class (inherits from BaseESPService):
     - Initialize with API key and server prefix
     - Implement `send_email()` using Mailchimp Transactional API
     - Implement `send_bulk_emails()` with campaign creation
     - Implement `add_subscriber()` to specific list
     - Implement `remove_subscriber()` with archive/delete options
     - Implement `update_subscriber()` with merge fields and tags
     - Handle Mailchimp-specific errors and rate limits

5. **Create ESP Factory:**
   - `apps/content/services/esp_factory.py`
   - `ESPFactory` class:
     - `get_esp_service()` - Return appropriate ESP service based on settings
     - Support for 'sendgrid', 'mailchimp', 'django' (fallback)
     - Singleton pattern for service instances

6. **Update Newsletter Model:**
   - `apps/content/models.py` - Update Newsletter model:
     - Add `esp_campaign_id` (CharField, null=True, blank=True)
     - Add `esp_provider` (CharField: 'sendgrid', 'mailchimp', 'django')
     - Add `sent_count` (IntegerField, default=0)
     - Add `delivered_count` (IntegerField, default=0)
     - Add `opened_count` (IntegerField, default=0)
     - Add `clicked_count` (IntegerField, default=0)
     - Add `bounced_count` (IntegerField, default=0)
     - Add `unsubscribed_count` (IntegerField, default=0)
     - Add `last_synced_at` (DateTimeField, null=True)
   - Add methods:
     - `calculate_open_rate()` - Return percentage
     - `calculate_click_rate()` - Return percentage
     - `sync_stats_from_esp()` - Fetch latest stats from ESP

7. **Create Email Event Model:**
   - `apps/content/models.py` - Add `EmailEvent` model
   - Fields:
     - `newsletter` (ForeignKey to Newsletter)
     - `subscriber` (ForeignKey to EmailSubscriber)
     - `event_type` (CharField: 'sent', 'delivered', 'opened', 'clicked', 'bounced', 'unsubscribed', 'spam_report')
     - `event_data` (JSONField, default=dict)
     - `esp_event_id` (CharField, unique=True, db_index=True)
     - `timestamp` (DateTimeField, auto_now_add=True, db_index=True)
     - `ip_address` (GenericIPAddressField, null=True)
     - `user_agent` (TextField, blank=True)
     - `url_clicked` (URLField, null=True, blank=True)
   - Meta:
     - indexes on (newsletter, event_type), (subscriber, event_type)

8. **Update Newsletter Sending Task:**
   - `apps/content/tasks.py` - Update `send_newsletter` task:
     - Use ESPFactory to get appropriate service
     - Batch subscribers (1000 per batch for SendGrid)
     - Track sending progress
     - Store esp_campaign_id
     - Handle ESP-specific errors
     - Log sending statistics
     - Update Newsletter.sent_count

9. **Create Webhook Handlers:**
   - `apps/content/views/webhook_views.py`
   - `SendGridWebhookView` class (APIView or CSRF-exempt view):
     - Verify webhook signature
     - Parse SendGrid event payload
     - Create EmailEvent records
     - Update Newsletter statistics
     - Update EmailSubscriber status (bounced, unsubscribed)
   - `MailchimpWebhookView` class:
     - Verify webhook signature
     - Parse Mailchimp event payload
     - Create EmailEvent records
     - Update statistics

10. **Create Webhook URLs:**
    - `apps/content/urls.py` - Add webhook endpoints:
      - `path('webhooks/sendgrid/', SendGridWebhookView.as_view(), name='sendgrid_webhook')`
      - `path('webhooks/mailchimp/', MailchimpWebhookView.as_view(), name='mailchimp_webhook')`

11. **Create Stats Sync Task:**
    - `apps/content/tasks.py` - Add `sync_newsletter_stats` task:
      - Fetch newsletters sent in last 30 days
      - For each newsletter, call sync_stats_from_esp()
      - Update delivered, opened, clicked counts
      - Log sync results
    - Add to Celery Beat: Run daily

12. **Create Analytics Dashboard:**
    - `apps/content/templates/content/newsletter_analytics.html`
    - Display for each newsletter:
      - Sent, delivered, opened, clicked counts
      - Open rate, click rate percentages
      - Bounce and unsubscribe counts
      - Event timeline
      - Top clicked links
    - Charts using Chart.js or similar

13. **Update Admin Interface:**
    - `apps/content/admin.py` - Update NewsletterAdmin:
      - Add readonly fields for ESP stats
      - Add action: `sync_stats_from_esp`
      - Add action: `resend_to_failed`
      - Display open rate and click rate in list
    - Add `EmailEventAdmin`:
      - List display: newsletter, subscriber, event_type, timestamp
      - List filters: event_type, timestamp
      - Search: subscriber email

**Acceptance Criteria:**
- SendGrid and Mailchimp services successfully send emails
- Bulk sending works with proper batching
- Subscriber management syncs with ESP
- Webhooks receive and process events correctly
- EmailEvent records created for all events
- Newsletter statistics update automatically
- Analytics dashboard displays accurate metrics
- Admin can view and sync ESP stats
- Bounce and unsubscribe handling works correctly
- Rate limiting and error handling prevent failures

**Files to Create:**
- `apps/content/services/esp_service.py`
- `apps/content/services/sendgrid_service.py`
- `apps/content/services/mailchimp_service.py`
- `apps/content/services/esp_factory.py`
- `apps/content/views/webhook_views.py`
- `apps/content/templates/content/newsletter_analytics.html`

**Files to Modify:**
- `apps/content/models.py` (update Newsletter, add EmailEvent)
- `apps/content/tasks.py` (update send_newsletter, add sync_newsletter_stats)
- `apps/content/admin.py` (update NewsletterAdmin, add EmailEventAdmin)
- `apps/content/urls.py` (add webhook URLs)
- `requirements/base.txt` (add sendgrid, mailchimp-marketing)
- `.env.example` (add ESP configuration)
- `config/settings/base.py` (add ESP_PROVIDER, SENDGRID_*, MAILCHIMP_* settings)

---

### TICKET-034: Advanced Monitoring - Scraper Health and AI Cost Tracking
**Priority:** MEDIUM | **Phase:** 5 | **Dependencies:** TICKET-009, TICKET-014, TICKET-030

**Description:**
Implement comprehensive monitoring dashboards for scraper health, AI API usage/costs, and system performance metrics with alerting capabilities.

**Requirements:**

1. **Create Scraper Health Model:**
   - `apps/aggregation/models.py` - Add `ScraperHealthLog` model
   - Fields:
     - `source` (ForeignKey to Source)
     - `spider_name` (CharField, max_length=100, db_index=True)
     - `run_timestamp` (DateTimeField, auto_now_add=True, db_index=True)
     - `status` (CharField: 'success', 'partial_success', 'failed', 'blocked', 'captcha')
     - `items_scraped` (IntegerField, default=0)
     - `items_failed` (IntegerField, default=0)
     - `duration_seconds` (FloatField)
     - `error_type` (CharField, null=True, blank=True)
     - `error_message` (TextField, blank=True)
     - `http_status_codes` (JSONField, default=dict, help_text="Count of each status code")
     - `retry_count` (IntegerField, default=0)
     - `memory_usage_mb` (FloatField, null=True)
     - `cpu_usage_percent` (FloatField, null=True)
   - Methods:
     - `is_healthy()` - Return boolean based on status and error rate
     - `calculate_success_rate()` - Return percentage

2. **Create AI Usage Tracking Model:**
   - `apps/content/models.py` - Add `AIUsageLog` model
   - Fields:
     - `timestamp` (DateTimeField, auto_now_add=True, db_index=True)
     - `provider` (CharField: 'openai', 'anthropic', db_index=True)
     - `model` (CharField, max_length=100, db_index=True)
     - `task_type` (CharField: 'article_generation', 'summary', 'moderation', 'avatar_response', db_index=True)
     - `prompt_tokens` (IntegerField)
     - `completion_tokens` (IntegerField)
     - `total_tokens` (IntegerField)
     - `estimated_cost_usd` (DecimalField, max_digits=10, decimal_places=6)
     - `latency_ms` (IntegerField, help_text="API call latency in milliseconds")
     - `success` (BooleanField, default=True, db_index=True)
     - `error_message` (TextField, blank=True)
     - `related_object_type` (CharField, null=True)
     - `related_object_id` (IntegerField, null=True)
   - Methods:
     - `calculate_cost()` - Calculate cost based on provider pricing
   - Meta:
     - indexes on (timestamp, provider), (task_type, timestamp)

3. **Update Scraping Tasks to Log Health:**
   - `apps/aggregation/tasks.py` - Update scraping tasks:
     - Track start time and end time
     - Count items scraped and failed
     - Capture memory and CPU usage
     - Log HTTP status codes encountered
     - Create ScraperHealthLog entry after each run
     - Handle exceptions and log error details

4. **Update AI Service to Log Usage:**
   - `apps/content/services/ai_service.py` - Update AIService:
     - Track tokens used in each API call
     - Calculate cost based on provider pricing
     - Measure API call latency
     - Create AIUsageLog entry for each call
     - Add context (task_type, related_object)

5. **Create Monitoring Service:**
   - `apps/core/services/monitoring_service.py`
   - `MonitoringService` class with methods:
     - `get_scraper_health_summary(days=7)` - Aggregate scraper stats
     - `get_failing_sources(threshold=0.5)` - Sources with low success rate
     - `get_blocked_sources()` - Sources encountering blocks/CAPTCHAs
     - `get_ai_usage_summary(days=30)` - Aggregate AI usage and costs
     - `get_ai_cost_by_task_type(days=30)` - Break down costs by task
     - `get_ai_cost_by_provider(days=30)` - Break down costs by provider
     - `calculate_daily_ai_cost()` - Current day's cost
     - `calculate_monthly_ai_cost()` - Current month's cost
     - `predict_monthly_ai_cost()` - Projection based on current usage
     - `get_system_health_score()` - Overall health score (0-100)

6. **Create Monitoring Dashboard Views:**
   - `apps/core/views/monitoring_views.py`
   - `ScraperHealthDashboardView` class:
     - Display scraper success rates over time
     - Show failing sources with error details
     - Display blocked sources
     - Show scraping volume trends
     - Alert indicators for sources needing attention
   - `AIUsageDashboardView` class:
     - Display daily/monthly AI costs
     - Show cost breakdown by task type
     - Show cost breakdown by provider
     - Display token usage trends
     - Show cost projections
     - Alert if approaching budget limits
   - `SystemHealthDashboardView` class:
     - Overall system health score
     - Celery queue lengths
     - Database performance metrics
     - Redis cache hit rates
     - Recent errors summary

7. **Create Dashboard Templates:**
   - `apps/core/templates/monitoring/scraper_health.html`
     - Charts: Success rate over time, items scraped per day
     - Table: Failing sources with error counts
     - Table: Blocked sources with last block time
   - `apps/core/templates/monitoring/ai_usage.html`
     - Charts: Daily cost, monthly cost trend, cost by task type
     - Metrics: Total tokens, average latency, success rate
     - Budget indicator: Current vs. target monthly cost
   - `apps/core/templates/monitoring/system_health.html`
     - Health score gauge
     - Service status indicators (DB, Redis, Celery)
     - Recent errors list
     - Performance metrics

8. **Create Alerting System:**
   - `apps/core/services/alerting_service.py`
   - `AlertingService` class with methods:
     - `check_scraper_health()` - Alert if sources failing
     - `check_ai_cost_budget()` - Alert if exceeding budget
     - `check_celery_queues()` - Alert if queues backing up
     - `check_error_rates()` - Alert if error rate spikes
     - `send_alert(alert_type, message, severity)` - Send via email/Slack
   - Alert channels:
     - Email to admins
     - Slack webhook (optional)
     - Django admin notifications

9. **Create Monitoring Tasks:**
   - `apps/core/tasks.py` - Add monitoring tasks:
     - `check_system_health()` - Run health checks and send alerts
     - `cleanup_old_logs(days=90)` - Delete old health/usage logs
     - `generate_daily_report()` - Email daily summary to admins
     - `generate_weekly_report()` - Email weekly summary
   - Add to Celery Beat:
     - Health checks: Every 15 minutes
     - Cleanup: Daily at 2 AM
     - Daily report: Daily at 8 AM
     - Weekly report: Monday at 9 AM

10. **Create Management Commands:**
    - `apps/core/management/commands/scraper_health_report.py`
      - Display scraper health summary in terminal
      - Show failing sources
      - Show blocked sources
    - `apps/core/management/commands/ai_cost_report.py`
      - Display AI usage and cost summary
      - Show breakdown by task type and provider
      - Show projections

11. **Create API Endpoints:**
    - `apps/core/api/monitoring_api.py`
    - REST API endpoints for external monitoring tools:
      - `/api/monitoring/scraper-health/` - JSON scraper health data
      - `/api/monitoring/ai-usage/` - JSON AI usage data
      - `/api/monitoring/system-health/` - JSON system health data
    - Require authentication (API key or token)

12. **Update Settings:**
    - `config/settings/base.py` - Add monitoring settings:
      - `MONITORING_ENABLED` = True
      - `ALERT_EMAIL_RECIPIENTS` = []
      - `SLACK_WEBHOOK_URL` = None
      - `AI_MONTHLY_BUDGET_USD` = 500.0
      - `AI_DAILY_BUDGET_USD` = 20.0
      - `SCRAPER_FAILURE_THRESHOLD` = 0.5 (50% failure rate)
      - `HEALTH_LOG_RETENTION_DAYS` = 90

13. **Create Admin Interface:**
    - `apps/aggregation/admin.py` - Add `ScraperHealthLogAdmin`
      - List display: source, spider_name, status, items_scraped, duration_seconds, run_timestamp
      - List filters: status, spider_name, run_timestamp
      - Search: source name, error_message
    - `apps/content/admin.py` - Add `AIUsageLogAdmin`
      - List display: timestamp, provider, model, task_type, total_tokens, estimated_cost_usd
      - List filters: provider, model, task_type, success, timestamp
      - Aggregation: Show total cost in changelist

**Acceptance Criteria:**
- ScraperHealthLog created after each scraping run
- AIUsageLog created for each AI API call
- Scraper health dashboard shows success rates and failing sources
- AI usage dashboard shows costs and projections
- System health dashboard shows overall status
- Alerts sent when thresholds exceeded
- Management commands provide CLI access to reports
- API endpoints return monitoring data in JSON
- Admin can view and filter health/usage logs
- Old logs automatically cleaned up
- Daily/weekly reports emailed to admins

**Files to Create:**
- `apps/core/services/monitoring_service.py`
- `apps/core/services/alerting_service.py`
- `apps/core/views/monitoring_views.py`
- `apps/core/templates/monitoring/scraper_health.html`
- `apps/core/templates/monitoring/ai_usage.html`
- `apps/core/templates/monitoring/system_health.html`
- `apps/core/api/monitoring_api.py`
- `apps/core/management/commands/scraper_health_report.py`
- `apps/core/management/commands/ai_cost_report.py`

**Files to Modify:**
- `apps/aggregation/models.py` (add ScraperHealthLog)
- `apps/content/models.py` (add AIUsageLog)
- `apps/aggregation/tasks.py` (add health logging)
- `apps/content/services/ai_service.py` (add usage logging)
- `apps/core/tasks.py` (add monitoring tasks)
- `apps/aggregation/admin.py` (add ScraperHealthLogAdmin)
- `apps/content/admin.py` (add AIUsageLogAdmin)
- `apps/core/urls.py` (add monitoring dashboard URLs)
- `config/settings/base.py` (add monitoring settings)
- `config/urls.py` (include monitoring API URLs)

---

## Summary

This comprehensive ticket list covers all major components of the frugal living platform:

**Phase 1 (Tickets 1-13):** Core infrastructure, database models, scraping, content processing, and basic frontend
**Phase 2 (Tickets 14-18):** AI integration, content generation, newsletter system, and email subscriptions
**Phase 3 (Tickets 19-23):** User management, forum implementation, topic/post creation
**Phase 4 (Tickets 24-30):** AI avatars, forum participation, content moderation, testing, and deployment
**Phase 5 (Tickets 31-34):** Advanced features - source discovery automation, JavaScript scraping, ESP integration, advanced monitoring

### Phase 5 Advanced Features:
- **TICKET-031:** Automated source discovery with AI-powered vetting and quality scoring
- **TICKET-032:** JavaScript rendering with Playwright and anti-detection measures
- **TICKET-033:** Enhanced newsletter distribution with SendGrid/Mailchimp integration and webhook tracking
- **TICKET-034:** Comprehensive monitoring dashboards for scraper health and AI cost tracking

Each ticket is:
- **Self-contained** with clear requirements and acceptance criteria
- **Dependency-aware** with explicit prerequisites
- **Implementation-ready** with specific file paths and technical details
- **Testable** with defined success criteria

The tickets can be executed sequentially by an AI coding agent, with each ticket building upon the previous ones to create a complete, production-ready platform with advanced automation and monitoring capabilities.

