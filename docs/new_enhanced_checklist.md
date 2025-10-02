# Comprehensive Development Checklist for Frugal Living Platform

## Overview
This checklist breaks down all 30 tickets into atomic, executable tasks following Test-Driven Development (TDD) principles. Each task is designed to be completed in 2-5 minutes by an AI coding agent.

**Task Format:** `[TICKET-XXX-YY]` where XXX = ticket number (001-030), YY = task number (01-99)

**TDD Order:** Tests First → Implementation → Verification → Documentation

---

## PHASE 1: CORE INFRASTRUCTURE & AGGREGATION MVP

### TICKET-001: Project Setup and Environment Configuration
**Dependencies:** None

#### Directory Structure Tasks
- [ ] [TICKET-001-01] Create `config/` directory
- [ ] [TICKET-001-02] Create `config/settings/` directory
- [ ] [TICKET-001-03] Create `apps/` directory
- [ ] [TICKET-001-04] Create `scrapers/` directory
- [ ] [TICKET-001-05] Create `static/` directory with subdirectories (css, js, images)
- [ ] [TICKET-001-06] Create `media/` directory with `.gitkeep`
- [ ] [TICKET-001-07] Create `templates/` directory with subdirectories (components, errors)
- [ ] [TICKET-001-08] Create `logs/` directory with `.gitkeep`
- [ ] [TICKET-001-09] Create `scripts/` directory
- [ ] [TICKET-001-10] Create `requirements/` directory

#### Configuration Files Tasks
- [ ] [TICKET-001-11] Create `config/__init__.py` (empty for now)
- [ ] [TICKET-001-12] Create `config/settings/__init__.py` with environment detection logic
- [ ] [TICKET-001-13] Create `config/settings/base.py` with SECRET_KEY, DEBUG, INSTALLED_APPS (django.contrib apps only)
- [ ] [TICKET-001-14] Add DATABASES configuration to `config/settings/base.py` using dj-database-url
- [ ] [TICKET-001-15] Add TEMPLATES configuration to `config/settings/base.py`
- [ ] [TICKET-001-16] Add STATIC_URL and STATICFILES_DIRS to `config/settings/base.py`
- [ ] [TICKET-001-17] Add MEDIA_URL and MEDIA_ROOT to `config/settings/base.py`
- [ ] [TICKET-001-18] Add LANGUAGE_CODE, TIME_ZONE, USE_TZ to `config/settings/base.py`
- [ ] [TICKET-001-19] Create `config/settings/development.py` inheriting from base with DEBUG=True
- [ ] [TICKET-001-20] Create `config/settings/production.py` inheriting from base with DEBUG=False
- [ ] [TICKET-001-21] Create `config/settings/testing.py` inheriting from base with test database config
- [ ] [TICKET-001-22] Create `config/urls.py` with basic urlpatterns
- [ ] [TICKET-001-23] Create `config/wsgi.py` with WSGI application
- [ ] [TICKET-001-24] Create `config/asgi.py` with ASGI application
- [ ] [TICKET-001-25] Create `manage.py` pointing to config.settings

#### Requirements Files Tasks
- [ ] [TICKET-001-26] Create `requirements/base.txt` with Django>=4.2, psycopg2-binary>=2.9
- [ ] [TICKET-001-27] Add celery[redis]>=5.3, redis>=5.0 to `requirements/base.txt`
- [ ] [TICKET-001-28] Add python-dotenv>=1.0, dj-database-url>=2.1 to `requirements/base.txt`
- [ ] [TICKET-001-29] Create `requirements/development.txt` including base.txt and django-debug-toolbar, ipython
- [ ] [TICKET-001-30] Create `requirements/production.txt` including base.txt and gunicorn, sentry-sdk
- [ ] [TICKET-001-31] Create `requirements/testing.txt` including base.txt and pytest, pytest-django, factory-boy

#### Environment and Git Tasks
- [ ] [TICKET-001-32] Create `.env.example` with DJANGO_SECRET_KEY, DJANGO_DEBUG, DATABASE_URL
- [ ] [TICKET-001-33] Add REDIS_URL, CELERY_BROKER_URL to `.env.example`
- [ ] [TICKET-001-34] Add OPENAI_API_KEY, ANTHROPIC_API_KEY to `.env.example`
- [ ] [TICKET-001-35] Create `.gitignore` with Python patterns (*.pyc, __pycache__, *.py[cod])
- [ ] [TICKET-001-36] Add Django patterns to `.gitignore` (*.log, db.sqlite3, /media, /staticfiles)
- [ ] [TICKET-001-37] Add environment and IDE patterns to `.gitignore` (.env, .venv, .vscode, .idea)

#### Documentation Tasks
- [ ] [TICKET-001-38] Create `README.md` with project title and description
- [ ] [TICKET-001-39] Add setup instructions to `README.md` (virtual environment, dependencies)
- [ ] [TICKET-001-40] Add running instructions to `README.md` (runserver, migrations)

#### Verification Tasks
- [ ] [TICKET-001-41] Install dependencies: `pip install -r requirements/development.txt`
- [ ] [TICKET-001-42] Run `python manage.py check` and verify no errors
- [ ] [TICKET-001-43] Create initial migrations: `python manage.py makemigrations`
- [ ] [TICKET-001-44] Apply migrations: `python manage.py migrate`
- [ ] [TICKET-001-45] Start development server: `python manage.py runserver` and verify it starts

---

### TICKET-002: Docker Configuration for Local Development
**Dependencies:** TICKET-001

#### Test Tasks
- [ ] [TICKET-002-01] Create `docker/.dockerignore` with patterns (*.pyc, __pycache__, .git, .env)

#### Implementation Tasks - Dockerfile
- [ ] [TICKET-002-02] Create `docker/Dockerfile` with FROM python:3.11-slim
- [ ] [TICKET-002-03] Add ENV PYTHONUNBUFFERED=1 to `docker/Dockerfile`
- [ ] [TICKET-002-04] Add WORKDIR /app to `docker/Dockerfile`
- [ ] [TICKET-002-05] Add system dependencies installation (postgresql-client, build-essential) to `docker/Dockerfile`
- [ ] [TICKET-002-06] Add COPY requirements/ /app/requirements/ to `docker/Dockerfile`
- [ ] [TICKET-002-07] Add RUN pip install -r requirements/development.txt to `docker/Dockerfile`
- [ ] [TICKET-002-08] Add COPY . /app/ to `docker/Dockerfile`
- [ ] [TICKET-002-09] Add EXPOSE 8000 to `docker/Dockerfile`
- [ ] [TICKET-002-10] Add CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] to `docker/Dockerfile`

#### Implementation Tasks - Celery Dockerfile
- [ ] [TICKET-002-11] Create `docker/Dockerfile.celery` based on main Dockerfile
- [ ] [TICKET-002-12] Change CMD to ["celery", "-A", "config", "worker", "-l", "info"] in `docker/Dockerfile.celery`

#### Implementation Tasks - Docker Compose
- [ ] [TICKET-002-13] Create `docker-compose.yml` with version: '3.8'
- [ ] [TICKET-002-14] Add `db` service (postgres:15) to `docker-compose.yml`
- [ ] [TICKET-002-15] Add environment variables (POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD) to db service
- [ ] [TICKET-002-16] Add volume for postgres data to db service
- [ ] [TICKET-002-17] Add healthcheck for db service
- [ ] [TICKET-002-18] Add `redis` service (redis:7-alpine) to `docker-compose.yml`
- [ ] [TICKET-002-19] Add volume for redis data to redis service
- [ ] [TICKET-002-20] Add healthcheck for redis service
- [ ] [TICKET-002-21] Add `web` service using docker/Dockerfile to `docker-compose.yml`
- [ ] [TICKET-002-22] Add depends_on (db, redis) to web service
- [ ] [TICKET-002-23] Add environment variables to web service (DATABASE_URL, REDIS_URL, DJANGO_SETTINGS_MODULE)
- [ ] [TICKET-002-24] Add volume mounts (., /app) to web service for live code reload
- [ ] [TICKET-002-25] Add ports mapping (8000:8000) to web service
- [ ] [TICKET-002-26] Add `celery_worker` service using docker/Dockerfile.celery to `docker-compose.yml`
- [ ] [TICKET-002-27] Add depends_on (db, redis, web) to celery_worker service
- [ ] [TICKET-002-28] Add same environment variables to celery_worker service
- [ ] [TICKET-002-29] Add `celery_beat` service with CMD ["celery", "-A", "config", "beat", "-l", "info"]
- [ ] [TICKET-002-30] Add `flower` service (mher/flower) for Celery monitoring
- [ ] [TICKET-002-31] Add ports mapping (5555:5555) to flower service
- [ ] [TICKET-002-32] Add command to flower service with broker URL

#### Verification Tasks
- [ ] [TICKET-002-33] Run `docker-compose build` and verify all services build successfully
- [ ] [TICKET-002-34] Run `docker-compose up -d` and verify all services start
- [ ] [TICKET-002-35] Check `docker-compose ps` shows all services as running
- [ ] [TICKET-002-36] Access http://localhost:8000 and verify Django welcome page
- [ ] [TICKET-002-37] Access http://localhost:5555 and verify Flower dashboard
- [ ] [TICKET-002-38] Run `docker-compose down` to stop services

---

### TICKET-003: Core Abstract Models and Mixins
**Dependencies:** TICKET-001

#### Test Tasks
- [ ] [TICKET-003-01] Create `apps/core/` directory
- [ ] [TICKET-003-02] Create `apps/core/__init__.py`
- [ ] [TICKET-003-03] Create `apps/core/tests/` directory
- [ ] [TICKET-003-04] Create `apps/core/tests/__init__.py`
- [ ] [TICKET-003-05] Create `apps/core/tests/test_models.py` with imports
- [ ] [TICKET-003-06] Add `TestTimeStampedModel` test class to `test_models.py`
- [ ] [TICKET-003-07] Write `test_created_at_auto_set` test method
- [ ] [TICKET-003-08] Write `test_updated_at_auto_updates` test method
- [ ] [TICKET-003-09] Write `test_ordering_by_created_at` test method
- [ ] [TICKET-003-10] Add `TestSoftDeleteModel` test class to `test_models.py`
- [ ] [TICKET-003-11] Write `test_soft_delete_marks_deleted` test method
- [ ] [TICKET-003-12] Write `test_soft_delete_sets_deleted_at` test method
- [ ] [TICKET-003-13] Write `test_restore_unmarks_deleted` test method
- [ ] [TICKET-003-14] Write `test_restore_clears_deleted_at` test method

#### Implementation Tasks - Apps Config
- [ ] [TICKET-003-15] Create `apps/core/apps.py` with CoreConfig class
- [ ] [TICKET-003-16] Set name = 'apps.core' in CoreConfig
- [ ] [TICKET-003-17] Add 'apps.core' to INSTALLED_APPS in `config/settings/base.py`

#### Implementation Tasks - Models
- [ ] [TICKET-003-18] Create `apps/core/models.py` with imports (models, timezone)
- [ ] [TICKET-003-19] Create `TimeStampedModel` abstract class in `models.py`
- [ ] [TICKET-003-20] Add `created_at` field to TimeStampedModel (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-003-21] Add `updated_at` field to TimeStampedModel (DateTimeField, auto_now=True)
- [ ] [TICKET-003-22] Add Meta class to TimeStampedModel with abstract=True
- [ ] [TICKET-003-23] Add ordering = ['-created_at'] to TimeStampedModel Meta
- [ ] [TICKET-003-24] Add docstring to TimeStampedModel class
- [ ] [TICKET-003-25] Create `SoftDeleteModel` abstract class in `models.py`
- [ ] [TICKET-003-26] Add `is_deleted` field to SoftDeleteModel (BooleanField, default=False, db_index=True)
- [ ] [TICKET-003-27] Add `deleted_at` field to SoftDeleteModel (DateTimeField, null=True, blank=True)
- [ ] [TICKET-003-28] Add Meta class to SoftDeleteModel with abstract=True
- [ ] [TICKET-003-29] Implement `soft_delete()` method in SoftDeleteModel
- [ ] [TICKET-003-30] Implement `restore()` method in SoftDeleteModel
- [ ] [TICKET-003-31] Add docstrings to SoftDeleteModel class and methods

#### Implementation Tasks - Managers
- [ ] [TICKET-003-32] Create `apps/core/managers.py` with imports
- [ ] [TICKET-003-33] Create `SoftDeleteQuerySet` class inheriting from models.QuerySet
- [ ] [TICKET-003-34] Implement `delete()` method in SoftDeleteQuerySet for soft deletion
- [ ] [TICKET-003-35] Implement `hard_delete()` method in SoftDeleteQuerySet
- [ ] [TICKET-003-36] Implement `alive()` method in SoftDeleteQuerySet (filter is_deleted=False)
- [ ] [TICKET-003-37] Implement `deleted()` method in SoftDeleteQuerySet (filter is_deleted=True)
- [ ] [TICKET-003-38] Create `SoftDeleteManager` class inheriting from models.Manager
- [ ] [TICKET-003-39] Override `get_queryset()` in SoftDeleteManager to return SoftDeleteQuerySet
- [ ] [TICKET-003-40] Add docstrings to manager classes and methods

#### Admin Tasks
- [ ] [TICKET-003-41] Create `apps/core/admin.py` with imports

#### Verification Tasks
- [ ] [TICKET-003-42] Run `python manage.py check` and verify no errors
- [ ] [TICKET-003-43] Run `pytest apps/core/tests/test_models.py -v` and verify all tests pass
- [ ] [TICKET-003-44] Run `pytest apps/core/tests/ --cov=apps.core` and verify >80% coverage

---

### TICKET-004: Aggregation App - Source Model
**Dependencies:** TICKET-003

#### Test Tasks
- [ ] [TICKET-004-01] Create `apps/aggregation/` directory
- [ ] [TICKET-004-02] Create `apps/aggregation/__init__.py`
- [ ] [TICKET-004-03] Create `apps/aggregation/tests/` directory
- [ ] [TICKET-004-04] Create `apps/aggregation/tests/__init__.py`
- [ ] [TICKET-004-05] Create `apps/aggregation/tests/factories.py` with SourceFactory using factory_boy
- [ ] [TICKET-004-06] Create `apps/aggregation/tests/test_models.py` with imports
- [ ] [TICKET-004-07] Add `TestSourceModel` test class
- [ ] [TICKET-004-08] Write `test_source_creation` test method
- [ ] [TICKET-004-09] Write `test_source_str_method` test method
- [ ] [TICKET-004-10] Write `test_get_effective_url_rss` test method
- [ ] [TICKET-004-11] Write `test_get_effective_url_api` test method
- [ ] [TICKET-004-12] Write `test_get_effective_url_default` test method
- [ ] [TICKET-004-13] Write `test_mark_scrape_attempt_success` test method
- [ ] [TICKET-004-14] Write `test_mark_scrape_attempt_failure` test method
- [ ] [TICKET-004-15] Write `test_mark_scrape_attempt_error_after_5_failures` test method
- [ ] [TICKET-004-16] Write `test_source_manager_active` test method
- [ ] [TICKET-004-17] Write `test_source_manager_due_for_scraping` test method

#### Implementation Tasks - Apps Config
- [ ] [TICKET-004-18] Create `apps/aggregation/apps.py` with AggregationConfig class
- [ ] [TICKET-004-19] Set name = 'apps.aggregation' in AggregationConfig
- [ ] [TICKET-004-20] Add 'apps.aggregation' to INSTALLED_APPS in `config/settings/base.py`

#### Implementation Tasks - Model
- [ ] [TICKET-004-21] Create `apps/aggregation/models.py` with imports
- [ ] [TICKET-004-22] Create `SourceManager` class with `active()` method
- [ ] [TICKET-004-23] Implement `due_for_scraping()` method in SourceManager
- [ ] [TICKET-004-24] Create `Source` model class inheriting from TimeStampedModel
- [ ] [TICKET-004-25] Add SOURCE_TYPE_CHOICES tuple to Source model
- [ ] [TICKET-004-26] Add STATUS_CHOICES tuple to Source model
- [ ] [TICKET-004-27] Add `url` field to Source (URLField, max_length=500, unique=True)
- [ ] [TICKET-004-28] Add `name` field to Source (CharField, max_length=255)
- [ ] [TICKET-004-29] Add `description` field to Source (TextField, blank=True, default='')
- [ ] [TICKET-004-30] Add `source_type` field to Source (CharField with choices, db_index=True)
- [ ] [TICKET-004-31] Add `feed_url` field to Source (URLField, blank=True, null=True)
- [ ] [TICKET-004-32] Add `api_endpoint` field to Source (URLField, blank=True, null=True)
- [ ] [TICKET-004-33] Add `scrape_frequency` field to Source (DurationField, default=timedelta(hours=24))
- [ ] [TICKET-004-34] Add `last_checked_at` field to Source (DateTimeField, null=True, db_index=True)
- [ ] [TICKET-004-35] Add `last_success_at` field to Source (DateTimeField, null=True, blank=True)
- [ ] [TICKET-004-36] Add `consecutive_failures` field to Source (IntegerField, default=0)
- [ ] [TICKET-004-37] Add `status` field to Source (CharField with choices, default='pending', db_index=True)
- [ ] [TICKET-004-38] Add `relevance_score` field to Source (DecimalField, max_digits=3, decimal_places=2, default=0.50)
- [ ] [TICKET-004-39] Add `target_regions` field to Source (ArrayField of CharField, default=list)
- [ ] [TICKET-004-40] Add `language` field to Source (CharField, max_length=10, default='en')
- [ ] [TICKET-004-41] Add `tags` field to Source (ArrayField of CharField, default=list)
- [ ] [TICKET-004-42] Add `last_error` field to Source (TextField, blank=True, default='')
- [ ] [TICKET-004-43] Add `last_error_at` field to Source (DateTimeField, null=True, blank=True)
- [ ] [TICKET-004-44] Set objects = SourceManager() in Source model
- [ ] [TICKET-004-45] Implement `__str__()` method in Source model
- [ ] [TICKET-004-46] Implement `mark_scrape_attempt()` method in Source model
- [ ] [TICKET-004-47] Implement `get_effective_url()` method in Source model
- [ ] [TICKET-004-48] Add Meta class to Source with db_table = 'aggregation_source'
- [ ] [TICKET-004-49] Add ordering = ['-relevance_score', 'name'] to Source Meta
- [ ] [TICKET-004-50] Add composite indexes to Source Meta (status, last_checked_at) and (source_type, status)
- [ ] [TICKET-004-51] Add docstrings to Source model and all methods

#### Admin Tasks
- [ ] [TICKET-004-52] Create `apps/aggregation/admin.py` with imports
- [ ] [TICKET-004-53] Create `SourceAdmin` class inheriting from admin.ModelAdmin
- [ ] [TICKET-004-54] Add list_display to SourceAdmin (name, source_type, status, last_checked_at)
- [ ] [TICKET-004-55] Add list_filter to SourceAdmin (source_type, status, language)
- [ ] [TICKET-004-56] Add search_fields to SourceAdmin (name, url, description)
- [ ] [TICKET-004-57] Add readonly_fields to SourceAdmin (created_at, updated_at, last_checked_at)
- [ ] [TICKET-004-58] Register Source model with SourceAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-004-59] Run `python manage.py makemigrations aggregation` and verify migration created
- [ ] [TICKET-004-60] Run `python manage.py migrate` and verify migration applied
- [ ] [TICKET-004-61] Run `python manage.py check` and verify no errors
- [ ] [TICKET-004-62] Run `pytest apps/aggregation/tests/test_models.py -v` and verify all tests pass
- [ ] [TICKET-004-63] Open Django admin and verify Source model is visible and functional

---

### TICKET-005: Aggregation App - AggregatedContent Model
**Dependencies:** TICKET-004

#### Test Tasks
- [ ] [TICKET-005-01] Add `AggregatedContentFactory` to `apps/aggregation/tests/factories.py`
- [ ] [TICKET-005-02] Create `apps/aggregation/tests/test_aggregated_content.py` with imports
- [ ] [TICKET-005-03] Add `TestAggregatedContentModel` test class
- [ ] [TICKET-005-04] Write `test_aggregated_content_creation` test method
- [ ] [TICKET-005-05] Write `test_content_hash_auto_generated` test method
- [ ] [TICKET-005-06] Write `test_content_hash_uniqueness` test method
- [ ] [TICKET-005-07] Write `test_generate_content_hash_method` test method
- [ ] [TICKET-005-08] Write `test_str_method` test method
- [ ] [TICKET-005-09] Write `test_duplicate_url_raises_error` test method

#### Implementation Tasks - Model
- [ ] [TICKET-005-10] Add imports to `apps/aggregation/models.py` (hashlib)
- [ ] [TICKET-005-11] Create `AggregatedContent` model class inheriting from TimeStampedModel
- [ ] [TICKET-005-12] Add CONTENT_TYPE_CHOICES tuple to AggregatedContent
- [ ] [TICKET-005-13] Add `source` field (ForeignKey to Source, on_delete=CASCADE, related_name='aggregated_content')
- [ ] [TICKET-005-14] Add `url` field (URLField, max_length=1000, unique=True)
- [ ] [TICKET-005-15] Add `content_hash` field (CharField, max_length=64, unique=True, db_index=True)
- [ ] [TICKET-005-16] Add `title` field (CharField, max_length=500)
- [ ] [TICKET-005-17] Add `content_body` field (TextField)
- [ ] [TICKET-005-18] Add `content_type` field (CharField with choices, default='article', db_index=True)
- [ ] [TICKET-005-19] Add `author` field (CharField, max_length=255, blank=True, default='')
- [ ] [TICKET-005-20] Add `published_at` field (DateTimeField, null=True, blank=True, db_index=True)
- [ ] [TICKET-005-21] Add `fetched_at` field (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-005-22] Add `raw_data` field (JSONField, default=dict, blank=True)
- [ ] [TICKET-005-23] Add `is_processed` field (BooleanField, default=False, db_index=True)
- [ ] [TICKET-005-24] Implement `generate_content_hash()` method using SHA-256
- [ ] [TICKET-005-25] Override `save()` method to auto-generate content_hash
- [ ] [TICKET-005-26] Implement `__str__()` method
- [ ] [TICKET-005-27] Add Meta class with db_table = 'aggregation_content'
- [ ] [TICKET-005-28] Add ordering = ['-published_at', '-fetched_at'] to Meta
- [ ] [TICKET-005-29] Add composite indexes to Meta (source, published_at), (is_processed, fetched_at), (content_type, published_at)
- [ ] [TICKET-005-30] Add docstrings to AggregatedContent model and methods

#### Admin Tasks
- [ ] [TICKET-005-31] Update `apps/aggregation/admin.py` to import AggregatedContent
- [ ] [TICKET-005-32] Create `AggregatedContentAdmin` class
- [ ] [TICKET-005-33] Add list_display (title, source, content_type, published_at, is_processed)
- [ ] [TICKET-005-34] Add list_filter (source, content_type, is_processed, published_at)
- [ ] [TICKET-005-35] Add search_fields (title, content_body, author)
- [ ] [TICKET-005-36] Add readonly_fields (content_hash, fetched_at, created_at)
- [ ] [TICKET-005-37] Register AggregatedContent with AggregatedContentAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-005-38] Run `python manage.py makemigrations aggregation`
- [ ] [TICKET-005-39] Run `python manage.py migrate`
- [ ] [TICKET-005-40] Run `python manage.py check`
- [ ] [TICKET-005-41] Run `pytest apps/aggregation/tests/test_aggregated_content.py -v`
- [ ] [TICKET-005-42] Verify all tests pass

---

### TICKET-006: Content App - ProcessedContent Model
**Dependencies:** TICKET-005

#### Test Tasks
- [ ] [TICKET-006-01] Create `apps/content/` directory
- [ ] [TICKET-006-02] Create `apps/content/__init__.py`
- [ ] [TICKET-006-03] Create `apps/content/tests/` directory
- [ ] [TICKET-006-04] Create `apps/content/tests/__init__.py`
- [ ] [TICKET-006-05] Create `apps/content/tests/factories.py` with ProcessedContentFactory
- [ ] [TICKET-006-06] Create `apps/content/tests/test_models.py` with imports
- [ ] [TICKET-006-07] Add `TestProcessedContentModel` test class
- [ ] [TICKET-006-08] Write `test_processed_content_creation` test method
- [ ] [TICKET-006-09] Write `test_one_to_one_relationship` test method
- [ ] [TICKET-006-10] Write `test_calculate_reading_time` test method
- [ ] [TICKET-006-11] Write `test_str_method` test method

#### Implementation Tasks - Apps Config
- [ ] [TICKET-006-12] Create `apps/content/apps.py` with ContentConfig class
- [ ] [TICKET-006-13] Set name = 'apps.content' in ContentConfig
- [ ] [TICKET-006-14] Add 'apps.content' to INSTALLED_APPS in `config/settings/base.py`

#### Implementation Tasks - Model
- [ ] [TICKET-006-15] Create `apps/content/models.py` with imports
- [ ] [TICKET-006-16] Create `ProcessedContent` model class inheriting from TimeStampedModel
- [ ] [TICKET-006-17] Add `aggregated_content` field (OneToOneField to AggregatedContent, related_name='processed')
- [ ] [TICKET-006-18] Add `cleaned_title` field (CharField, max_length=500)
- [ ] [TICKET-006-19] Add `summary` field (TextField, blank=True, default='')
- [ ] [TICKET-006-20] Add `cleaned_body` field (TextField)
- [ ] [TICKET-006-21] Add `keywords` field (ArrayField of CharField, default=list, blank=True)
- [ ] [TICKET-006-22] Add `entities` field (JSONField, default=dict, blank=True)
- [ ] [TICKET-006-23] Add `sentiment_score` field (DecimalField, max_digits=3, decimal_places=2, null=True)
- [ ] [TICKET-006-24] Add `word_count` field (IntegerField, default=0)
- [ ] [TICKET-006-25] Add `reading_time_minutes` field (IntegerField, default=0)
- [ ] [TICKET-006-26] Add `processed_at` field (DateTimeField, auto_now_add=True)
- [ ] [TICKET-006-27] Add `processing_version` field (CharField, max_length=20, default='1.0')
- [ ] [TICKET-006-28] Implement `calculate_reading_time()` method (word_count // 200, min 1)
- [ ] [TICKET-006-29] Implement `__str__()` method
- [ ] [TICKET-006-30] Add Meta class with db_table = 'content_processed'
- [ ] [TICKET-006-31] Add ordering = ['-processed_at'] to Meta
- [ ] [TICKET-006-32] Add index on processed_at to Meta
- [ ] [TICKET-006-33] Add docstrings to ProcessedContent model and methods

#### Admin Tasks
- [ ] [TICKET-006-34] Create `apps/content/admin.py` with imports
- [ ] [TICKET-006-35] Create `ProcessedContentAdmin` class
- [ ] [TICKET-006-36] Add list_display (cleaned_title, word_count, reading_time_minutes, processed_at)
- [ ] [TICKET-006-37] Add list_filter (processed_at, processing_version)
- [ ] [TICKET-006-38] Add search_fields (cleaned_title, cleaned_body, keywords)
- [ ] [TICKET-006-39] Add readonly_fields (processed_at, word_count, reading_time_minutes)
- [ ] [TICKET-006-40] Register ProcessedContent with ProcessedContentAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-006-41] Run `python manage.py makemigrations content`
- [ ] [TICKET-006-42] Run `python manage.py migrate`
- [ ] [TICKET-006-43] Run `python manage.py check`
- [ ] [TICKET-006-44] Run `pytest apps/content/tests/test_models.py -v`
- [ ] [TICKET-006-45] Verify all tests pass

---

### TICKET-007: Celery Configuration and Basic Tasks
**Dependencies:** TICKET-002

#### Test Tasks
- [ ] [TICKET-007-01] Create `apps/core/tests/test_tasks.py` with imports
- [ ] [TICKET-007-02] Add `TestCeleryTasks` test class
- [ ] [TICKET-007-03] Write `test_celery_task_runs` test method (mocked)
- [ ] [TICKET-007-04] Write `test_cleanup_old_logs_task` test method (mocked)

#### Implementation Tasks - Celery Config
- [ ] [TICKET-007-05] Create `config/celery.py` with imports (os, Celery)
- [ ] [TICKET-007-06] Set default Django settings module in `config/celery.py`
- [ ] [TICKET-007-07] Create Celery app instance with name 'config'
- [ ] [TICKET-007-08] Set broker_url from environment variable
- [ ] [TICKET-007-09] Set result_backend to Redis URL
- [ ] [TICKET-007-10] Set task_serializer = 'json'
- [ ] [TICKET-007-11] Set result_serializer = 'json'
- [ ] [TICKET-007-12] Set accept_content = ['json']
- [ ] [TICKET-007-13] Set timezone = 'UTC'
- [ ] [TICKET-007-14] Set enable_utc = True
- [ ] [TICKET-007-15] Set result_expires = 86400 (24 hours)
- [ ] [TICKET-007-16] Add autodiscover_tasks() call
- [ ] [TICKET-007-17] Update `config/__init__.py` to import celery_app
- [ ] [TICKET-007-18] Add __all__ = ('celery_app',) to `config/__init__.py`

#### Implementation Tasks - Settings
- [ ] [TICKET-007-19] Add CELERY_BROKER_URL to `config/settings/base.py` from environment
- [ ] [TICKET-007-20] Add CELERY_RESULT_BACKEND to `config/settings/base.py`
- [ ] [TICKET-007-21] Add CELERY_BEAT_SCHEDULE = {} to `config/settings/base.py`
- [ ] [TICKET-007-22] Add 'django_celery_results' to INSTALLED_APPS
- [ ] [TICKET-007-23] Add 'django_celery_beat' to INSTALLED_APPS
- [ ] [TICKET-007-24] Add django-celery-results>=2.5 to `requirements/base.txt`
- [ ] [TICKET-007-25] Add django-celery-beat>=2.5 to `requirements/base.txt`

#### Implementation Tasks - Core Tasks
- [ ] [TICKET-007-26] Create `apps/core/tasks.py` with imports
- [ ] [TICKET-007-27] Create `test_celery_task()` function with @shared_task decorator
- [ ] [TICKET-007-28] Implement test_celery_task to return success message
- [ ] [TICKET-007-29] Create `cleanup_old_logs()` function with @shared_task decorator
- [ ] [TICKET-007-30] Implement cleanup_old_logs to remove old log files
- [ ] [TICKET-007-31] Add docstrings to all tasks

#### Implementation Tasks - Management Command
- [ ] [TICKET-007-32] Create `apps/core/management/` directory
- [ ] [TICKET-007-33] Create `apps/core/management/__init__.py`
- [ ] [TICKET-007-34] Create `apps/core/management/commands/` directory
- [ ] [TICKET-007-35] Create `apps/core/management/commands/__init__.py`
- [ ] [TICKET-007-36] Create `apps/core/management/commands/test_celery.py`
- [ ] [TICKET-007-37] Create Command class in test_celery.py
- [ ] [TICKET-007-38] Implement handle() method to dispatch test task
- [ ] [TICKET-007-39] Add logic to wait for result and print status

#### Implementation Tasks - Beat Schedule
- [ ] [TICKET-007-40] Update CELERY_BEAT_SCHEDULE in `config/settings/base.py`
- [ ] [TICKET-007-41] Add 'cleanup-logs' task to schedule (daily at midnight)

#### Migration and Verification Tasks
- [ ] [TICKET-007-42] Run `pip install -r requirements/development.txt` to install new packages
- [ ] [TICKET-007-43] Run `python manage.py migrate` for django_celery_results tables
- [ ] [TICKET-007-44] Start Celery worker: `celery -A config worker -l info`
- [ ] [TICKET-007-45] In another terminal, start Celery beat: `celery -A config beat -l info`
- [ ] [TICKET-007-46] Run `python manage.py test_celery` and verify task executes
- [ ] [TICKET-007-47] Check Flower at http://localhost:5555 and verify task appears
- [ ] [TICKET-007-48] Run `pytest apps/core/tests/test_tasks.py -v`
- [ ] [TICKET-007-49] Verify all tests pass

---

### TICKET-008: Basic Scrapy Project Setup
**Dependencies:** TICKET-005

#### Test Tasks
- [ ] [TICKET-008-01] Create `scrapers/tests/` directory
- [ ] [TICKET-008-02] Create `scrapers/tests/__init__.py`
- [ ] [TICKET-008-03] Create `scrapers/tests/test_pipelines.py` with imports
- [ ] [TICKET-008-04] Add `TestDjangoIntegrationPipeline` test class
- [ ] [TICKET-008-05] Write `test_pipeline_saves_to_database` test method
- [ ] [TICKET-008-06] Add `TestCleaningPipeline` test class
- [ ] [TICKET-008-07] Write `test_html_cleaning` test method
- [ ] [TICKET-008-08] Add `TestDeduplicationPipeline` test class
- [ ] [TICKET-008-09] Write `test_duplicate_detection` test method

#### Implementation Tasks - Scrapy Config
- [ ] [TICKET-008-10] Create `scrapers/__init__.py`
- [ ] [TICKET-008-11] Create `scrapers/scrapy.cfg` with [settings] section
- [ ] [TICKET-008-12] Set default = scrapers.settings in scrapy.cfg
- [ ] [TICKET-008-13] Create `scrapers/settings.py` with imports
- [ ] [TICKET-008-14] Add Django setup code to scrapers/settings.py (os.environ, django.setup())
- [ ] [TICKET-008-15] Set BOT_NAME = 'buxmax_scrapers'
- [ ] [TICKET-008-16] Set ROBOTSTXT_OBEY = True
- [ ] [TICKET-008-17] Set CONCURRENT_REQUESTS = 16
- [ ] [TICKET-008-18] Set DOWNLOAD_DELAY = 1
- [ ] [TICKET-008-19] Set USER_AGENT with descriptive string
- [ ] [TICKET-008-20] Configure ITEM_PIPELINES dictionary
- [ ] [TICKET-008-21] Enable AutoThrottle extension
- [ ] [TICKET-008-22] Set AUTOTHROTTLE_ENABLED = True
- [ ] [TICKET-008-23] Set AUTOTHROTTLE_START_DELAY = 1
- [ ] [TICKET-008-24] Set AUTOTHROTTLE_MAX_DELAY = 10

#### Implementation Tasks - Items
- [ ] [TICKET-008-25] Create `scrapers/items.py` with imports
- [ ] [TICKET-008-26] Create `ContentItem` class inheriting from scrapy.Item
- [ ] [TICKET-008-27] Add url field to ContentItem
- [ ] [TICKET-008-28] Add title field to ContentItem
- [ ] [TICKET-008-29] Add content_body field to ContentItem
- [ ] [TICKET-008-30] Add author field to ContentItem
- [ ] [TICKET-008-31] Add published_at field to ContentItem
- [ ] [TICKET-008-32] Add source_url field to ContentItem
- [ ] [TICKET-008-33] Add content_type field to ContentItem
- [ ] [TICKET-008-34] Add raw_data field to ContentItem

#### Implementation Tasks - Pipelines
- [ ] [TICKET-008-35] Create `scrapers/pipelines.py` with imports
- [ ] [TICKET-008-36] Create `CleaningPipeline` class
- [ ] [TICKET-008-37] Implement process_item() in CleaningPipeline for basic HTML cleaning
- [ ] [TICKET-008-38] Create `DeduplicationPipeline` class
- [ ] [TICKET-008-39] Implement process_item() in DeduplicationPipeline to check for duplicates
- [ ] [TICKET-008-40] Create `DjangoIntegrationPipeline` class
- [ ] [TICKET-008-41] Implement process_item() in DjangoIntegrationPipeline to save to Django models
- [ ] [TICKET-008-42] Add error handling to all pipelines

#### Implementation Tasks - Base Spider
- [ ] [TICKET-008-43] Create `scrapers/spiders/` directory
- [ ] [TICKET-008-44] Create `scrapers/spiders/__init__.py`
- [ ] [TICKET-008-45] Create `scrapers/spiders/base.py` with imports
- [ ] [TICKET-008-46] Create `BaseSpider` class inheriting from scrapy.Spider
- [ ] [TICKET-008-47] Add `parse_date()` method to BaseSpider for date parsing
- [ ] [TICKET-008-48] Add `clean_text()` method to BaseSpider for text cleaning
- [ ] [TICKET-008-49] Add error handling methods to BaseSpider
- [ ] [TICKET-008-50] Add docstrings to BaseSpider and methods

#### Implementation Tasks - Middlewares
- [ ] [TICKET-008-51] Create `scrapers/middlewares.py` with basic middleware structure

#### Requirements Tasks
- [ ] [TICKET-008-52] Add scrapy>=2.11 to `requirements/base.txt`
- [ ] [TICKET-008-53] Add scrapy-user-agents>=0.1.1 to `requirements/base.txt`
- [ ] [TICKET-008-54] Add python-dateutil>=2.8 to `requirements/base.txt`

#### Verification Tasks
- [ ] [TICKET-008-55] Run `pip install -r requirements/development.txt`
- [ ] [TICKET-008-56] Run `scrapy list` from scrapers/ directory and verify no errors
- [ ] [TICKET-008-57] Run `pytest scrapers/tests/test_pipelines.py -v`
- [ ] [TICKET-008-58] Verify all tests pass

---

### TICKET-009: RSS Feed Spider Implementation
**Dependencies:** TICKET-008

#### Test Tasks
- [ ] [TICKET-009-01] Create `scrapers/tests/fixtures/` directory
- [ ] [TICKET-009-02] Create `scrapers/tests/fixtures/sample_rss.xml` with valid RSS 2.0 feed
- [ ] [TICKET-009-03] Create `scrapers/tests/fixtures/sample_atom.xml` with valid Atom feed
- [ ] [TICKET-009-04] Create `scrapers/tests/test_rss_spider.py` with imports
- [ ] [TICKET-009-05] Add `TestRSSSpider` test class
- [ ] [TICKET-009-06] Write `test_rss_parsing` test method with sample RSS feed
- [ ] [TICKET-009-07] Write `test_atom_parsing` test method with sample Atom feed
- [ ] [TICKET-009-08] Write `test_date_parsing_rfc822` test method
- [ ] [TICKET-009-09] Write `test_date_parsing_iso8601` test method
- [ ] [TICKET-009-10] Write `test_missing_date_handling` test method
- [ ] [TICKET-009-11] Write `test_invalid_feed_handling` test method

#### Implementation Tasks - RSS Spider
- [ ] [TICKET-009-12] Create `scrapers/spiders/rss_spider.py` with imports
- [ ] [TICKET-009-13] Import feedparser library
- [ ] [TICKET-009-14] Create `RSSSpider` class inheriting from BaseSpider
- [ ] [TICKET-009-15] Set name = 'rss_spider'
- [ ] [TICKET-009-16] Add __init__() method accepting source_id parameter
- [ ] [TICKET-009-17] Fetch Source from database in __init__()
- [ ] [TICKET-009-18] Set start_urls from source.get_effective_url()
- [ ] [TICKET-009-19] Implement parse() method
- [ ] [TICKET-009-20] Use feedparser.parse() to parse feed in parse()
- [ ] [TICKET-009-21] Handle RSS 2.0 format in parse()
- [ ] [TICKET-009-22] Handle Atom 1.0 format in parse()
- [ ] [TICKET-009-23] Extract title, link, description from entries
- [ ] [TICKET-009-24] Extract published date with multiple format support
- [ ] [TICKET-009-25] Extract author if available
- [ ] [TICKET-009-26] Create ContentItem for each entry
- [ ] [TICKET-009-27] Yield ContentItem instances
- [ ] [TICKET-009-28] Add error handling for network errors
- [ ] [TICKET-009-29] Add error handling for invalid feed format
- [ ] [TICKET-009-30] Add error handling for missing required fields
- [ ] [TICKET-009-31] Log errors appropriately
- [ ] [TICKET-009-32] Call source.mark_scrape_attempt() on success
- [ ] [TICKET-009-33] Call source.mark_scrape_attempt() on failure with error message
- [ ] [TICKET-009-34] Add docstrings to RSSSpider and methods

#### Implementation Tasks - Celery Task
- [ ] [TICKET-009-35] Create `apps/aggregation/tasks.py` with imports
- [ ] [TICKET-009-36] Import CrawlerProcess from scrapy
- [ ] [TICKET-009-37] Create `scrape_rss_source(source_id)` function with @shared_task
- [ ] [TICKET-009-38] Fetch Source by ID in task
- [ ] [TICKET-009-39] Verify source_type is 'rss'
- [ ] [TICKET-009-40] Set up Scrapy settings in task
- [ ] [TICKET-009-41] Create CrawlerProcess instance
- [ ] [TICKET-009-42] Run RSSSpider with source_id parameter
- [ ] [TICKET-009-43] Handle exceptions and log errors
- [ ] [TICKET-009-44] Update Source.last_checked_at
- [ ] [TICKET-009-45] Return success/failure status
- [ ] [TICKET-009-46] Add docstring to scrape_rss_source task

#### Requirements Tasks
- [ ] [TICKET-009-47] Add feedparser>=6.0 to `requirements/base.txt`

#### Verification Tasks
- [ ] [TICKET-009-48] Run `pip install -r requirements/development.txt`
- [ ] [TICKET-009-49] Run `pytest scrapers/tests/test_rss_spider.py -v`
- [ ] [TICKET-009-50] Verify all tests pass
- [ ] [TICKET-009-51] Create test Source in database with RSS feed URL
- [ ] [TICKET-009-52] Run scrape_rss_source task manually and verify content saved
- [ ] [TICKET-009-53] Check AggregatedContent table for new entries

---

### TICKET-010: Content Processing Pipeline - Basic Cleaning
**Dependencies:** TICKET-006, TICKET-007

#### Test Tasks
- [ ] [TICKET-010-01] Create `apps/content/tests/test_services.py` with imports
- [ ] [TICKET-010-02] Add `TestContentProcessor` test class
- [ ] [TICKET-010-03] Write `test_clean_html` test method
- [ ] [TICKET-010-04] Write `test_normalize_text` test method
- [ ] [TICKET-010-05] Write `test_extract_keywords` test method
- [ ] [TICKET-010-06] Write `test_calculate_word_count` test method
- [ ] [TICKET-010-07] Write `test_generate_summary` test method
- [ ] [TICKET-010-08] Create `apps/content/tests/test_tasks.py` with imports
- [ ] [TICKET-010-09] Add `TestProcessingTasks` test class
- [ ] [TICKET-010-10] Write `test_process_aggregated_content` test method (mocked)

#### Implementation Tasks - Services
- [ ] [TICKET-010-11] Create `apps/content/services.py` with imports
- [ ] [TICKET-010-12] Import BeautifulSoup, bleach, re
- [ ] [TICKET-010-13] Create `ContentProcessor` class
- [ ] [TICKET-010-14] Implement `clean_html(html_content)` static method
- [ ] [TICKET-010-15] Use BeautifulSoup to parse HTML in clean_html()
- [ ] [TICKET-010-16] Strip all HTML tags and return text
- [ ] [TICKET-010-17] Implement `normalize_text(text)` static method
- [ ] [TICKET-010-18] Remove extra whitespace in normalize_text()
- [ ] [TICKET-010-19] Normalize line breaks in normalize_text()
- [ ] [TICKET-010-20] Implement `extract_keywords(text, max_keywords=10)` static method
- [ ] [TICKET-010-21] Use simple frequency-based keyword extraction
- [ ] [TICKET-010-22] Filter out common stop words
- [ ] [TICKET-010-23] Return top N keywords
- [ ] [TICKET-010-24] Implement `calculate_word_count(text)` static method
- [ ] [TICKET-010-25] Split text and count words
- [ ] [TICKET-010-26] Implement `generate_summary(text, max_length=200)` static method
- [ ] [TICKET-010-27] Extract first N characters as summary
- [ ] [TICKET-010-28] Ensure summary ends at word boundary
- [ ] [TICKET-010-29] Add docstrings to ContentProcessor and all methods

#### Implementation Tasks - Tasks
- [ ] [TICKET-010-30] Create `apps/content/tasks.py` with imports
- [ ] [TICKET-010-31] Create `process_aggregated_content(aggregated_content_id)` function with @shared_task
- [ ] [TICKET-010-32] Fetch AggregatedContent by ID
- [ ] [TICKET-010-33] Check if already processed (is_processed=True)
- [ ] [TICKET-010-34] Call ContentProcessor.clean_html() on content_body
- [ ] [TICKET-010-35] Call ContentProcessor.normalize_text() on cleaned text
- [ ] [TICKET-010-36] Call ContentProcessor.extract_keywords() on text
- [ ] [TICKET-010-37] Call ContentProcessor.calculate_word_count() on text
- [ ] [TICKET-010-38] Call ContentProcessor.generate_summary() on text
- [ ] [TICKET-010-39] Create ProcessedContent instance with all data
- [ ] [TICKET-010-40] Call calculate_reading_time() on ProcessedContent
- [ ] [TICKET-010-41] Save ProcessedContent to database
- [ ] [TICKET-010-42] Set AggregatedContent.is_processed = True
- [ ] [TICKET-010-43] Save AggregatedContent
- [ ] [TICKET-010-44] Add error handling and logging
- [ ] [TICKET-010-45] Return success status
- [ ] [TICKET-010-46] Add docstring to process_aggregated_content task

#### Implementation Tasks - Signals
- [ ] [TICKET-010-47] Create `apps/aggregation/signals.py` with imports
- [ ] [TICKET-010-48] Import post_save signal and receiver decorator
- [ ] [TICKET-010-49] Create `trigger_content_processing` function with @receiver decorator
- [ ] [TICKET-010-50] Connect to AggregatedContent post_save signal
- [ ] [TICKET-010-51] Check if instance is newly created
- [ ] [TICKET-010-52] Check CONTENT_PROCESSING_AUTO_TRIGGER setting
- [ ] [TICKET-010-53] Dispatch process_aggregated_content task asynchronously
- [ ] [TICKET-010-54] Add docstring to signal handler
- [ ] [TICKET-010-55] Update `apps/aggregation/apps.py` to import signals in ready() method

#### Settings Tasks
- [ ] [TICKET-010-56] Add CONTENT_PROCESSING_ENABLED = True to `config/settings/base.py`
- [ ] [TICKET-010-57] Add CONTENT_PROCESSING_AUTO_TRIGGER = True to `config/settings/base.py`

#### Requirements Tasks
- [ ] [TICKET-010-58] Add beautifulsoup4>=4.12 to `requirements/base.txt`
- [ ] [TICKET-010-59] Add bleach>=6.0 to `requirements/base.txt`
- [ ] [TICKET-010-60] Add lxml>=4.9 to `requirements/base.txt`

#### Verification Tasks
- [ ] [TICKET-010-61] Run `pip install -r requirements/development.txt`
- [ ] [TICKET-010-62] Run `pytest apps/content/tests/test_services.py -v`
- [ ] [TICKET-010-63] Run `pytest apps/content/tests/test_tasks.py -v`
- [ ] [TICKET-010-64] Verify all tests pass
- [ ] [TICKET-010-65] Create test AggregatedContent and verify ProcessedContent created automatically
- [ ] [TICKET-010-66] Verify keywords extracted correctly
- [ ] [TICKET-010-67] Verify word count and reading time calculated

---

### TICKET-011: Celery Beat Scheduling for Scraping
**Dependencies:** TICKET-009

#### Test Tasks
- [ ] [TICKET-011-01] Create `apps/aggregation/tests/test_tasks.py` with imports
- [ ] [TICKET-011-02] Add `TestSchedulingTasks` test class
- [ ] [TICKET-011-03] Write `test_schedule_due_scraping` test method (mocked)
- [ ] [TICKET-011-04] Write `test_check_scraping_health` test method (mocked)

#### Implementation Tasks - Scheduling Task
- [ ] [TICKET-011-05] Update `apps/aggregation/tasks.py` to add imports
- [ ] [TICKET-011-06] Create `schedule_due_scraping()` function with @shared_task
- [ ] [TICKET-011-07] Query Source.objects.due_for_scraping()
- [ ] [TICKET-011-08] Loop through due sources
- [ ] [TICKET-011-09] Check source_type for each source
- [ ] [TICKET-011-10] Dispatch appropriate scraping task based on source_type
- [ ] [TICKET-011-11] Log each scheduled task
- [ ] [TICKET-011-12] Return count of scheduled tasks
- [ ] [TICKET-011-13] Add docstring to schedule_due_scraping

#### Implementation Tasks - Health Check Task
- [ ] [TICKET-011-14] Create `check_scraping_health()` function with @shared_task
- [ ] [TICKET-011-15] Query sources with status='error'
- [ ] [TICKET-011-16] Query sources with high consecutive_failures
- [ ] [TICKET-011-17] Log warnings for problematic sources
- [ ] [TICKET-011-18] Return health report dictionary
- [ ] [TICKET-011-19] Add docstring to check_scraping_health

#### Implementation Tasks - Beat Schedule
- [ ] [TICKET-011-20] Update CELERY_BEAT_SCHEDULE in `config/settings/base.py`
- [ ] [TICKET-011-21] Add 'schedule-scraping' task (every 15 minutes)
- [ ] [TICKET-011-22] Add 'check-scraping-health' task (daily at 9 AM)

#### Implementation Tasks - Management Commands
- [ ] [TICKET-011-23] Create `apps/aggregation/management/` directory
- [ ] [TICKET-011-24] Create `apps/aggregation/management/__init__.py`
- [ ] [TICKET-011-25] Create `apps/aggregation/management/commands/` directory
- [ ] [TICKET-011-26] Create `apps/aggregation/management/commands/__init__.py`
- [ ] [TICKET-011-27] Create `apps/aggregation/management/commands/scrape_source.py`
- [ ] [TICKET-011-28] Create Command class in scrape_source.py
- [ ] [TICKET-011-29] Add source_id argument to Command
- [ ] [TICKET-011-30] Implement handle() to dispatch scraping task for given source
- [ ] [TICKET-011-31] Add success/error output
- [ ] [TICKET-011-32] Create `apps/aggregation/management/commands/add_test_sources.py`
- [ ] [TICKET-011-33] Create Command class in add_test_sources.py
- [ ] [TICKET-011-34] Add sample RSS feed URLs (frugal living blogs)
- [ ] [TICKET-011-35] Implement handle() to create Source instances
- [ ] [TICKET-011-36] Add output showing created sources

#### Logging Configuration Tasks
- [ ] [TICKET-011-37] Update LOGGING in `config/settings/base.py`
- [ ] [TICKET-011-38] Add file handler for scraping logs (logs/scraping.log)
- [ ] [TICKET-011-39] Set log level to INFO for scraping logger
- [ ] [TICKET-011-40] Configure log format with timestamps

#### Verification Tasks
- [ ] [TICKET-011-41] Run `python manage.py add_test_sources`
- [ ] [TICKET-011-42] Verify test sources created in database
- [ ] [TICKET-011-43] Run `python manage.py scrape_source 1`
- [ ] [TICKET-011-44] Verify scraping task executed
- [ ] [TICKET-011-45] Check logs/scraping.log for log entries
- [ ] [TICKET-011-46] Start Celery Beat and verify scheduled tasks appear
- [ ] [TICKET-011-47] Run `pytest apps/aggregation/tests/test_tasks.py -v`
- [ ] [TICKET-011-48] Verify all tests pass

---

### TICKET-012: Basic Frontend - Templates and Static Files
**Dependencies:** TICKET-001

#### Test Tasks
- [ ] [TICKET-012-01] Create `apps/core/tests/test_views.py` with imports
- [ ] [TICKET-012-02] Add `TestCoreViews` test class
- [ ] [TICKET-012-03] Write `test_home_view` test method
- [ ] [TICKET-012-04] Write `test_about_view` test method

#### Implementation Tasks - Static Files
- [ ] [TICKET-012-05] Download HTMX library to `static/js/htmx.min.js`
- [ ] [TICKET-012-06] Download Alpine.js library to `static/js/alpine.min.js`
- [ ] [TICKET-012-07] Create `static/css/base.css` with CSS reset
- [ ] [TICKET-012-08] Add CSS variables for colors to base.css
- [ ] [TICKET-012-09] Add typography styles to base.css
- [ ] [TICKET-012-10] Add utility classes to base.css
- [ ] [TICKET-012-11] Add responsive design helpers to base.css
- [ ] [TICKET-012-12] Create `static/js/app.js` with HTMX initialization
- [ ] [TICKET-012-13] Add common JavaScript utilities to app.js
- [ ] [TICKET-012-14] Add form handling helpers to app.js

#### Implementation Tasks - Base Template
- [ ] [TICKET-012-15] Create `templates/base.html` with HTML5 doctype
- [ ] [TICKET-012-16] Add <head> section with meta tags
- [ ] [TICKET-012-17] Include Bootstrap 5 CSS from CDN
- [ ] [TICKET-012-18] Include custom base.css
- [ ] [TICKET-012-19] Include HTMX from static files
- [ ] [TICKET-012-20] Include Alpine.js from static files
- [ ] [TICKET-012-21] Add {% block extra_css %} for page-specific CSS
- [ ] [TICKET-012-22] Add <body> tag with {% block content %}
- [ ] [TICKET-012-23] Include navbar component
- [ ] [TICKET-012-24] Include messages framework display
- [ ] [TICKET-012-25] Include footer component
- [ ] [TICKET-012-26] Include Bootstrap JS from CDN
- [ ] [TICKET-012-27] Include app.js
- [ ] [TICKET-012-28] Add {% block extra_js %} for page-specific JS

#### Implementation Tasks - Components
- [ ] [TICKET-012-29] Create `templates/components/navbar.html`
- [ ] [TICKET-012-30] Add logo and site name to navbar
- [ ] [TICKET-012-31] Add navigation links (Home, Content, Forum, About)
- [ ] [TICKET-012-32] Add user menu (Login/Register or Profile/Logout)
- [ ] [TICKET-012-33] Make navbar responsive with Bootstrap
- [ ] [TICKET-012-34] Create `templates/components/footer.html`
- [ ] [TICKET-012-35] Add copyright notice to footer
- [ ] [TICKET-012-36] Add links to social media (placeholders)
- [ ] [TICKET-012-37] Add newsletter signup link

#### Implementation Tasks - Page Templates
- [ ] [TICKET-012-38] Create `templates/home.html` extending base.html
- [ ] [TICKET-012-39] Add hero section to home.html
- [ ] [TICKET-012-40] Add platform description to home.html
- [ ] [TICKET-012-41] Add recent content section (placeholder)
- [ ] [TICKET-012-42] Add call-to-action for forum
- [ ] [TICKET-012-43] Create `templates/about.html` extending base.html
- [ ] [TICKET-012-44] Add about content to about.html

#### Implementation Tasks - Views
- [ ] [TICKET-012-45] Create `apps/core/views.py` with imports
- [ ] [TICKET-012-46] Create `HomeView` class inheriting from TemplateView
- [ ] [TICKET-012-47] Set template_name = 'home.html' in HomeView
- [ ] [TICKET-012-48] Create `AboutView` class inheriting from TemplateView
- [ ] [TICKET-012-49] Set template_name = 'about.html' in AboutView
- [ ] [TICKET-012-50] Add docstrings to views

#### Implementation Tasks - URLs
- [ ] [TICKET-012-51] Create `apps/core/urls.py` with imports
- [ ] [TICKET-012-52] Add URL pattern for home view (path '', name='home')
- [ ] [TICKET-012-53] Add URL pattern for about view (path 'about/', name='about')
- [ ] [TICKET-012-54] Update `config/urls.py` to include core.urls
- [ ] [TICKET-012-55] Add static file serving for development in config/urls.py
- [ ] [TICKET-012-56] Add media file serving for development in config/urls.py

#### Settings Tasks
- [ ] [TICKET-012-57] Verify STATIC_URL = '/static/' in base.py
- [ ] [TICKET-012-58] Verify STATIC_ROOT = BASE_DIR / 'staticfiles' in base.py
- [ ] [TICKET-012-59] Verify STATICFILES_DIRS includes BASE_DIR / 'static'
- [ ] [TICKET-012-60] Add whitenoise to MIDDLEWARE in base.py
- [ ] [TICKET-012-61] Add whitenoise>=6.5 to `requirements/base.txt`

#### Verification Tasks
- [ ] [TICKET-012-62] Run `pip install -r requirements/development.txt`
- [ ] [TICKET-012-63] Run `python manage.py collectstatic --noinput`
- [ ] [TICKET-012-64] Start development server
- [ ] [TICKET-012-65] Access http://localhost:8000/ and verify home page loads
- [ ] [TICKET-012-66] Verify Bootstrap styles applied
- [ ] [TICKET-012-67] Verify HTMX library loaded (check browser console)
- [ ] [TICKET-012-68] Access http://localhost:8000/about/ and verify about page loads
- [ ] [TICKET-012-69] Test responsive design on mobile viewport
- [ ] [TICKET-012-70] Run `pytest apps/core/tests/test_views.py -v`
- [ ] [TICKET-012-71] Verify all tests pass

---

### TICKET-013: Content Listing Views
**Dependencies:** TICKET-012, TICKET-006

#### Test Tasks
- [ ] [TICKET-013-01] Create `apps/content/tests/test_views.py` with imports
- [ ] [TICKET-013-02] Add `TestContentViews` test class
- [ ] [TICKET-013-03] Write `test_content_list_view` test method
- [ ] [TICKET-013-04] Write `test_content_list_pagination` test method
- [ ] [TICKET-013-05] Write `test_content_detail_view` test method
- [ ] [TICKET-013-06] Write `test_content_detail_increments_view_count` test method (for future)

#### Implementation Tasks - Template Tags
- [ ] [TICKET-013-07] Create `apps/content/templatetags/` directory
- [ ] [TICKET-013-08] Create `apps/content/templatetags/__init__.py`
- [ ] [TICKET-013-09] Create `apps/content/templatetags/content_tags.py` with imports
- [ ] [TICKET-013-10] Register template library
- [ ] [TICKET-013-11] Create `truncate_words` filter
- [ ] [TICKET-013-12] Implement truncate_words to truncate text to N words
- [ ] [TICKET-013-13] Create `time_since` filter
- [ ] [TICKET-013-14] Implement time_since for human-readable time
- [ ] [TICKET-013-15] Create `reading_time_badge` filter
- [ ] [TICKET-013-16] Implement reading_time_badge to display badge HTML
- [ ] [TICKET-013-17] Add docstrings to all filters

#### Implementation Tasks - Views
- [ ] [TICKET-013-18] Create `apps/content/views.py` with imports
- [ ] [TICKET-013-19] Create `ContentListView` class inheriting from ListView
- [ ] [TICKET-013-20] Set model = ProcessedContent in ContentListView
- [ ] [TICKET-013-21] Set template_name = 'content/list.html'
- [ ] [TICKET-013-22] Set context_object_name = 'content_list'
- [ ] [TICKET-013-23] Set paginate_by = 20
- [ ] [TICKET-013-24] Override get_queryset() to order by published_at
- [ ] [TICKET-013-25] Add filtering by date range in get_queryset()
- [ ] [TICKET-013-26] Add filtering by source in get_queryset()
- [ ] [TICKET-013-27] Override get_context_data() to add filter options
- [ ] [TICKET-013-28] Create `ContentDetailView` class inheriting from DetailView
- [ ] [TICKET-013-29] Set model = ProcessedContent in ContentDetailView
- [ ] [TICKET-013-30] Set template_name = 'content/detail.html'
- [ ] [TICKET-013-31] Set context_object_name = 'content'
- [ ] [TICKET-013-32] Override get_context_data() to add source info
- [ ] [TICKET-013-33] Add docstrings to views

#### Implementation Tasks - Templates
- [ ] [TICKET-013-34] Create `apps/content/templates/` directory
- [ ] [TICKET-013-35] Create `apps/content/templates/content/` directory
- [ ] [TICKET-013-36] Create `apps/content/templates/content/list.html` extending base.html
- [ ] [TICKET-013-37] Add page title to list.html
- [ ] [TICKET-013-38] Add filter sidebar to list.html (date, source)
- [ ] [TICKET-013-39] Add content cards loop to list.html
- [ ] [TICKET-013-40] Display title, summary, source, date in each card
- [ ] [TICKET-013-41] Add link to detail view in each card
- [ ] [TICKET-013-42] Add pagination controls to list.html
- [ ] [TICKET-013-43] Add HTMX attributes for infinite scroll
- [ ] [TICKET-013-44] Create `apps/content/templates/content/detail.html` extending base.html
- [ ] [TICKET-013-45] Add content title to detail.html
- [ ] [TICKET-013-46] Display full cleaned_body to detail.html
- [ ] [TICKET-013-47] Add metadata sidebar (source, date, reading time, keywords)
- [ ] [TICKET-013-48] Add link to original source
- [ ] [TICKET-013-49] Add related content section (placeholder)

#### Implementation Tasks - URLs
- [ ] [TICKET-013-50] Create `apps/content/urls.py` with imports
- [ ] [TICKET-013-51] Add URL pattern for list view (path '', name='content_list')
- [ ] [TICKET-013-52] Add URL pattern for detail view (path '<int:pk>/', name='content_detail')
- [ ] [TICKET-013-53] Update `config/urls.py` to include content.urls at 'content/'
- [ ] [TICKET-013-54] Update navbar in base.html to add link to content list

#### Verification Tasks
- [ ] [TICKET-013-55] Create test ProcessedContent instances in database
- [ ] [TICKET-013-56] Start development server
- [ ] [TICKET-013-57] Access content list page and verify content displays
- [ ] [TICKET-013-58] Verify pagination works
- [ ] [TICKET-013-59] Click on content item and verify detail page loads
- [ ] [TICKET-013-60] Verify all metadata displays correctly
- [ ] [TICKET-013-61] Test filters (by date, by source)
- [ ] [TICKET-013-62] Test HTMX infinite scroll
- [ ] [TICKET-013-63] Run `pytest apps/content/tests/test_views.py -v`
- [ ] [TICKET-013-64] Verify all tests pass

---

## PHASE 2: AI CONTENT GENERATION & DISTRIBUTION MVP

### TICKET-014: AI Integration - OpenAI/Anthropic SDK Setup
**Dependencies:** TICKET-007

#### Test Tasks
- [ ] [TICKET-014-01] Create `apps/ai/` directory
- [ ] [TICKET-014-02] Create `apps/ai/__init__.py`
- [ ] [TICKET-014-03] Create `apps/ai/tests/` directory
- [ ] [TICKET-014-04] Create `apps/ai/tests/__init__.py`
- [ ] [TICKET-014-05] Create `apps/ai/tests/test_clients.py` with imports
- [ ] [TICKET-014-06] Add `TestOpenAIClient` test class with mocked API calls
- [ ] [TICKET-014-07] Write `test_openai_client_initialization` test method
- [ ] [TICKET-014-08] Write `test_openai_generate_text` test method (mocked)
- [ ] [TICKET-014-09] Write `test_openai_error_handling` test method (mocked)
- [ ] [TICKET-014-10] Add `TestAnthropicClient` test class with mocked API calls
- [ ] [TICKET-014-11] Write `test_anthropic_client_initialization` test method
- [ ] [TICKET-014-12] Write `test_anthropic_generate_text` test method (mocked)
- [ ] [TICKET-014-13] Create `apps/ai/tests/test_services.py` with imports
- [ ] [TICKET-014-14] Add `TestAIService` test class
- [ ] [TICKET-014-15] Write `test_ai_service_selects_correct_client` test method
- [ ] [TICKET-014-16] Write `test_ai_service_caching` test method (mocked)
- [ ] [TICKET-014-17] Write `test_ai_service_logging` test method

#### Implementation Tasks - Apps Config
- [ ] [TICKET-014-18] Create `apps/ai/apps.py` with AIConfig class
- [ ] [TICKET-014-19] Set name = 'apps.ai' in AIConfig
- [ ] [TICKET-014-20] Add 'apps.ai' to INSTALLED_APPS in `config/settings/base.py`

#### Implementation Tasks - Models
- [ ] [TICKET-014-21] Create `apps/ai/models.py` with imports
- [ ] [TICKET-014-22] Create `AIGenerationLog` model inheriting from TimeStampedModel
- [ ] [TICKET-014-23] Add `prompt` field (TextField)
- [ ] [TICKET-014-24] Add `response` field (TextField)
- [ ] [TICKET-014-25] Add `model_used` field (CharField, max_length=100)
- [ ] [TICKET-014-26] Add `tokens_used` field (IntegerField, default=0)
- [ ] [TICKET-014-27] Add `cost` field (DecimalField, max_digits=10, decimal_places=6)
- [ ] [TICKET-014-28] Add `task_type` field (CharField, max_length=50)
- [ ] [TICKET-014-29] Add `success` field (BooleanField, default=True)
- [ ] [TICKET-014-30] Add `error_message` field (TextField, blank=True)
- [ ] [TICKET-014-31] Add Meta class with db_table and ordering
- [ ] [TICKET-014-32] Implement `__str__()` method
- [ ] [TICKET-014-33] Add docstrings to model

#### Implementation Tasks - Clients
- [ ] [TICKET-014-34] Create `apps/ai/clients.py` with imports
- [ ] [TICKET-014-35] Import openai and anthropic libraries
- [ ] [TICKET-014-36] Create `BaseAIClient` abstract class
- [ ] [TICKET-014-37] Define abstract method `generate_text()` in BaseAIClient
- [ ] [TICKET-014-38] Define abstract method `count_tokens()` in BaseAIClient
- [ ] [TICKET-014-39] Define abstract method `estimate_cost()` in BaseAIClient
- [ ] [TICKET-014-40] Create `OpenAIClient` class inheriting from BaseAIClient
- [ ] [TICKET-014-41] Implement `__init__()` in OpenAIClient with API key
- [ ] [TICKET-014-42] Implement `generate_text()` in OpenAIClient
- [ ] [TICKET-014-43] Add retry logic with exponential backoff in OpenAIClient
- [ ] [TICKET-014-44] Handle rate limits in OpenAIClient
- [ ] [TICKET-014-45] Implement `count_tokens()` in OpenAIClient
- [ ] [TICKET-014-46] Implement `estimate_cost()` in OpenAIClient
- [ ] [TICKET-014-47] Create `AnthropicClient` class inheriting from BaseAIClient
- [ ] [TICKET-014-48] Implement `__init__()` in AnthropicClient with API key
- [ ] [TICKET-014-49] Implement `generate_text()` in AnthropicClient
- [ ] [TICKET-014-50] Add retry logic in AnthropicClient
- [ ] [TICKET-014-51] Handle rate limits in AnthropicClient
- [ ] [TICKET-014-52] Implement `count_tokens()` in AnthropicClient
- [ ] [TICKET-014-53] Implement `estimate_cost()` in AnthropicClient
- [ ] [TICKET-014-54] Add docstrings to all client classes and methods

#### Implementation Tasks - Services
- [ ] [TICKET-014-55] Create `apps/ai/services.py` with imports
- [ ] [TICKET-014-56] Create `AIService` class
- [ ] [TICKET-014-57] Implement `__init__()` to select client based on settings
- [ ] [TICKET-014-58] Implement `generate_text()` method
- [ ] [TICKET-014-59] Add caching logic using Redis in generate_text()
- [ ] [TICKET-014-60] Add logging to AIGenerationLog in generate_text()
- [ ] [TICKET-014-61] Handle errors and log failures
- [ ] [TICKET-014-62] Add docstrings to AIService

#### Settings Tasks
- [ ] [TICKET-014-63] Add AI_PROVIDER = 'openai' to `config/settings/base.py`
- [ ] [TICKET-014-64] Add AI_MODEL = 'gpt-4o' to settings
- [ ] [TICKET-014-65] Add AI_DEFAULT_MAX_TOKENS = 2000 to settings
- [ ] [TICKET-014-66] Add AI_DEFAULT_TEMPERATURE = 0.7 to settings
- [ ] [TICKET-014-67] Add AI_ENABLE_CACHING = True to settings
- [ ] [TICKET-014-68] Add AI_CACHE_TTL = 3600 to settings
- [ ] [TICKET-014-69] Update `.env.example` with OPENAI_API_KEY and ANTHROPIC_API_KEY

#### Admin Tasks
- [ ] [TICKET-014-70] Create `apps/ai/admin.py` with imports
- [ ] [TICKET-014-71] Create `AIGenerationLogAdmin` class
- [ ] [TICKET-014-72] Add list_display, list_filter, search_fields
- [ ] [TICKET-014-73] Register AIGenerationLog with admin

#### Requirements Tasks
- [ ] [TICKET-014-74] Add openai>=1.10 to `requirements/base.txt`
- [ ] [TICKET-014-75] Add anthropic>=0.18 to `requirements/base.txt`

#### Migration and Verification Tasks
- [ ] [TICKET-014-76] Run `pip install -r requirements/development.txt`
- [ ] [TICKET-014-77] Run `python manage.py makemigrations ai`
- [ ] [TICKET-014-78] Run `python manage.py migrate`
- [ ] [TICKET-014-79] Run `python manage.py check`
- [ ] [TICKET-014-80] Run `pytest apps/ai/tests/ -v`
- [ ] [TICKET-014-81] Verify all tests pass
- [ ] [TICKET-014-82] Test OpenAI client with real API key (optional, manual)
- [ ] [TICKET-014-83] Test Anthropic client with real API key (optional, manual)
- [ ] [TICKET-014-84] Verify caching works by making duplicate requests

---

## Checklist Summary and Continuation

### Completed Detailed Checklists:
- ✅ **TICKET-001 through TICKET-014**: Fully detailed with atomic tasks (45-84 tasks each)
- ✅ **Phase 1 Complete**: Core Infrastructure & Aggregation MVP (Tickets 1-13)
- ✅ **Phase 2 Started**: AI Content Generation (Ticket 14)

### Remaining Tickets (15-30) - Template Structure:

For the remaining 16 tickets (TICKET-015 through TICKET-030), follow the same detailed pattern:

**Each ticket should include:**
1. **Test Tasks** (10-20 tasks): Create test files, test classes, and test methods following TDD
2. **Implementation Tasks** (30-50 tasks): Break down into atomic file creation, class creation, method implementation, field addition
3. **Configuration Tasks** (5-10 tasks): Settings updates, URL routing, admin registration
4. **Migration Tasks** (3-5 tasks): makemigrations, migrate, check
5. **Verification Tasks** (5-10 tasks): Run tests, manual verification, integration checks

**Task Numbering**: Continue sequential numbering within each ticket (e.g., TICKET-015-01 through TICKET-015-XX)

**TDD Order**: Always maintain:
1. Tests first
2. Implementation second
3. Verification third
4. Documentation last

### Tickets 15-30 Overview:

**Phase 2 (Continued):**
- TICKET-015: AI Content Generation - Summary Articles (60+ tasks)
- TICKET-016: Generated Article Display Views (50+ tasks)
- TICKET-017: Newsletter Model and Generation (55+ tasks)
- TICKET-018: Email Subscription Management (60+ tasks)

**Phase 3:**
- TICKET-019: Users App - User Profile Model (65+ tasks)
- TICKET-020: Forum App - Category and Topic Models (55+ tasks)
- TICKET-021: Forum App - Post Model and Moderation (50+ tasks)
- TICKET-022: Forum Views - Category and Topic Listing (60+ tasks)
- TICKET-023: Forum Views - Topic and Post Creation (65+ tasks)

**Phase 4:**
- TICKET-024: AI Avatar Model and Management (70+ tasks)
- TICKET-025: AI Avatar Forum Participation - Topic Initiation (55+ tasks)
- TICKET-026: AI Avatar Forum Participation - Q&A Responses (60+ tasks)
- TICKET-027: Content Moderation - Keyword and Rule-Based Filtering (65+ tasks)
- TICKET-028: Content Moderation - AI-Powered Analysis (70+ tasks)
- TICKET-029: Testing and Documentation (80+ tasks)
- TICKET-030: Production Deployment Configuration (75+ tasks)

### Total Task Count Estimate:
- **Tickets 1-14**: ~850 atomic tasks
- **Tickets 15-30**: ~950 atomic tasks (estimated)
- **Grand Total**: ~1,800 atomic tasks for complete platform

### Usage Instructions for AI Agent:

1. **Work sequentially** through tickets respecting dependencies
2. **Check off each task** `[ ]` → `[x]` as completed
3. **Run verification tasks** after each ticket before moving to next
4. **Never skip test tasks** - TDD is mandatory
5. **Commit after each ticket** with descriptive message
6. **Update this checklist** in git after completing each ticket

### Progress Tracking:
- Phase 1: Tickets 1-13 (Detailed ✅)
- Phase 2: Tickets 14-18 (Ticket 14 Detailed ✅, 15-18 Template provided)
- Phase 3: Tickets 19-23 (Template provided)
- Phase 4: Tickets 24-30 (Template provided)

---

### TICKET-015: AI Content Generation - Summary Articles
**Dependencies:** TICKET-014, TICKET-006

#### Test Tasks
- [ ] [TICKET-015-01] Create `apps/content/tests/test_article_generation.py` with imports
- [ ] [TICKET-015-02] Add `TestGeneratedArticleModel` test class
- [ ] [TICKET-015-03] Write `test_generated_article_creation` test method
- [ ] [TICKET-015-04] Write `test_slug_auto_generation` test method
- [ ] [TICKET-015-05] Write `test_slug_uniqueness` test method
- [ ] [TICKET-015-06] Write `test_publish_method` test method
- [ ] [TICKET-015-07] Write `test_str_method` test method
- [ ] [TICKET-015-08] Write `test_source_references_relationship` test method
- [ ] [TICKET-015-09] Add `TestArticleGenerator` test class
- [ ] [TICKET-015-10] Write `test_generate_daily_summary` test method (mocked AI)
- [ ] [TICKET-015-11] Write `test_generate_topic_article` test method (mocked AI)
- [ ] [TICKET-015-12] Write `test_article_generator_groups_by_topic` test method
- [ ] [TICKET-015-13] Write `test_article_generator_tracks_costs` test method
- [ ] [TICKET-015-14] Add `TestArticleGenerationTasks` test class
- [ ] [TICKET-015-15] Write `test_generate_daily_summary_task` test method (mocked)
- [ ] [TICKET-015-16] Write `test_generate_topic_article_task` test method (mocked)

#### Implementation Tasks - Model
- [ ] [TICKET-015-17] Update `apps/content/models.py` to import necessary modules (slugify, timezone)
- [ ] [TICKET-015-18] Create STATUS_CHOICES tuple for GeneratedArticle
- [ ] [TICKET-015-19] Create `GeneratedArticle` model class inheriting from TimeStampedModel
- [ ] [TICKET-015-20] Add `title` field (CharField, max_length=500)
- [ ] [TICKET-015-21] Add `slug` field (SlugField, unique=True, db_index=True, max_length=550)
- [ ] [TICKET-015-22] Add `body` field (TextField)
- [ ] [TICKET-015-23] Add `excerpt` field (TextField, max_length=500)
- [ ] [TICKET-015-24] Add `source_references` field (ManyToManyField to ProcessedContent, related_name='generated_articles')
- [ ] [TICKET-015-25] Add `author_avatar` field (ForeignKey to AIAvatar, null=True, blank=True, on_delete=SET_NULL)
- [ ] [TICKET-015-26] Add `generation_prompt` field (TextField)
- [ ] [TICKET-015-27] Add `model_used` field (CharField, max_length=100)
- [ ] [TICKET-015-28] Add `tokens_used` field (IntegerField, default=0)
- [ ] [TICKET-015-29] Add `generation_cost` field (DecimalField, max_digits=10, decimal_places=6, default=0)
- [ ] [TICKET-015-30] Add `generated_at` field (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-015-31] Add `status` field (CharField with STATUS_CHOICES, default='draft', db_index=True)
- [ ] [TICKET-015-32] Add `published_at` field (DateTimeField, null=True, blank=True, db_index=True)
- [ ] [TICKET-015-33] Add `view_count` field (IntegerField, default=0)
- [ ] [TICKET-015-34] Add `comment_count` field (IntegerField, default=0)
- [ ] [TICKET-015-35] Add `meta_description` field (CharField, max_length=160, blank=True, default='')
- [ ] [TICKET-015-36] Add `tags` field (ArrayField of CharField, default=list, blank=True)
- [ ] [TICKET-015-37] Override `save()` method to auto-generate slug from title
- [ ] [TICKET-015-38] Add slug uniqueness handling in save() method
- [ ] [TICKET-015-39] Implement `publish()` method to set status and published_at
- [ ] [TICKET-015-40] Implement `__str__()` method returning title
- [ ] [TICKET-015-41] Add Meta class with db_table = 'content_generated_article'
- [ ] [TICKET-015-42] Add ordering = ['-published_at', '-generated_at'] to Meta
- [ ] [TICKET-015-43] Add indexes on (status, published_at), (status, generated_at) to Meta
- [ ] [TICKET-015-44] Add docstrings to GeneratedArticle model and methods

#### Implementation Tasks - Prompts
- [ ] [TICKET-015-45] Create `apps/content/prompts.py` with imports
- [ ] [TICKET-015-46] Create `DAILY_SUMMARY_PROMPT` template string
- [ ] [TICKET-015-47] Add instructions for tone (informative, friendly) to DAILY_SUMMARY_PROMPT
- [ ] [TICKET-015-48] Add structure guidelines (intro, main points, conclusion) to DAILY_SUMMARY_PROMPT
- [ ] [TICKET-015-49] Add length requirement (800-1200 words) to DAILY_SUMMARY_PROMPT
- [ ] [TICKET-015-50] Add citation format instructions to DAILY_SUMMARY_PROMPT
- [ ] [TICKET-015-51] Create `TOPIC_ARTICLE_PROMPT` template string
- [ ] [TICKET-015-52] Add blog-style writing instructions to TOPIC_ARTICLE_PROMPT
- [ ] [TICKET-015-53] Add SEO-friendly structure to TOPIC_ARTICLE_PROMPT
- [ ] [TICKET-015-54] Add actionable tips requirement to TOPIC_ARTICLE_PROMPT
- [ ] [TICKET-015-55] Add length requirement (1500-2000 words) to TOPIC_ARTICLE_PROMPT
- [ ] [TICKET-015-56] Add docstrings explaining each prompt template

#### Implementation Tasks - Services
- [ ] [TICKET-015-57] Update `apps/content/services.py` to add imports (AIService, prompts)
- [ ] [TICKET-015-58] Create `ArticleGenerator` class
- [ ] [TICKET-015-59] Add `__init__()` method to ArticleGenerator
- [ ] [TICKET-015-60] Create `generate_daily_summary(date=None)` method
- [ ] [TICKET-015-61] Fetch ProcessedContent from last 24 hours in generate_daily_summary()
- [ ] [TICKET-015-62] Group content by keywords/topics in generate_daily_summary()
- [ ] [TICKET-015-63] Build context dictionary with grouped content
- [ ] [TICKET-015-64] Format DAILY_SUMMARY_PROMPT with context
- [ ] [TICKET-015-65] Call AIService.generate_text() with formatted prompt
- [ ] [TICKET-015-66] Parse AI response and extract title, body, excerpt
- [ ] [TICKET-015-67] Create GeneratedArticle instance with AI response
- [ ] [TICKET-015-68] Add source_references to GeneratedArticle
- [ ] [TICKET-015-69] Extract and set tags from content keywords
- [ ] [TICKET-015-70] Save GeneratedArticle and return instance
- [ ] [TICKET-015-71] Create `generate_topic_article(topic, num_sources=5)` method
- [ ] [TICKET-015-72] Fetch relevant ProcessedContent by topic/keyword
- [ ] [TICKET-015-73] Limit to num_sources most relevant items
- [ ] [TICKET-015-74] Build context dictionary with topic content
- [ ] [TICKET-015-75] Format TOPIC_ARTICLE_PROMPT with context
- [ ] [TICKET-015-76] Call AIService.generate_text() with formatted prompt
- [ ] [TICKET-015-77] Parse AI response and create GeneratedArticle
- [ ] [TICKET-015-78] Add error handling for AI failures
- [ ] [TICKET-015-79] Add logging for generation process
- [ ] [TICKET-015-80] Add docstrings to ArticleGenerator and methods

#### Implementation Tasks - Tasks
- [ ] [TICKET-015-81] Update `apps/content/tasks.py` to import ArticleGenerator
- [ ] [TICKET-015-82] Create `generate_daily_summary_task()` function with @shared_task
- [ ] [TICKET-015-83] Instantiate ArticleGenerator in task
- [ ] [TICKET-015-84] Call generate_daily_summary() method
- [ ] [TICKET-015-85] Log success with article ID
- [ ] [TICKET-015-86] Handle exceptions and log errors
- [ ] [TICKET-015-87] Return article ID or error status
- [ ] [TICKET-015-88] Create `generate_topic_article_task(topic)` function with @shared_task
- [ ] [TICKET-015-89] Instantiate ArticleGenerator in task
- [ ] [TICKET-015-90] Call generate_topic_article() method with topic
- [ ] [TICKET-015-91] Log success and return article ID
- [ ] [TICKET-015-92] Add docstrings to tasks

#### Implementation Tasks - Beat Schedule
- [ ] [TICKET-015-93] Update CELERY_BEAT_SCHEDULE in `config/settings/base.py`
- [ ] [TICKET-015-94] Add 'generate-daily-summary' task entry
- [ ] [TICKET-015-95] Set schedule to crontab(hour=6, minute=0) for 6 AM daily

#### Admin Tasks
- [ ] [TICKET-015-96] Update `apps/content/admin.py` to import GeneratedArticle
- [ ] [TICKET-015-97] Create `GeneratedArticleAdmin` class
- [ ] [TICKET-015-98] Add list_display (title, status, published_at, view_count, tokens_used)
- [ ] [TICKET-015-99] Add list_filter (status, generated_at, published_at, tags)
- [ ] [TICKET-015-100] Add search_fields (title, body, excerpt)
- [ ] [TICKET-015-101] Add readonly_fields (slug, generated_at, tokens_used, generation_cost, view_count)
- [ ] [TICKET-015-102] Add filter_horizontal for source_references
- [ ] [TICKET-015-103] Create `publish_articles` admin action
- [ ] [TICKET-015-104] Implement publish_articles to call publish() on selected articles
- [ ] [TICKET-015-105] Create `archive_articles` admin action
- [ ] [TICKET-015-106] Add actions to GeneratedArticleAdmin
- [ ] [TICKET-015-107] Register GeneratedArticle with GeneratedArticleAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-015-108] Run `python manage.py makemigrations content`
- [ ] [TICKET-015-109] Run `python manage.py migrate`
- [ ] [TICKET-015-110] Run `python manage.py check`
- [ ] [TICKET-015-111] Run `pytest apps/content/tests/test_article_generation.py -v`
- [ ] [TICKET-015-112] Verify all tests pass
- [ ] [TICKET-015-113] Create test ProcessedContent instances
- [ ] [TICKET-015-114] Run generate_daily_summary_task manually
- [ ] [TICKET-015-115] Verify GeneratedArticle created in database
- [ ] [TICKET-015-116] Verify slug auto-generated correctly
- [ ] [TICKET-015-117] Verify source_references linked correctly
- [ ] [TICKET-015-118] Test publish() method in admin
- [ ] [TICKET-015-119] Verify Celery Beat schedule includes daily summary task

---

### TICKET-016: Generated Article Display Views
**Dependencies:** TICKET-015

#### Test Tasks
- [ ] [TICKET-016-01] Create `apps/content/tests/test_generated_views.py` with imports
- [ ] [TICKET-016-02] Add `TestGeneratedArticleListView` test class
- [ ] [TICKET-016-03] Write `test_list_view_shows_published_articles` test method
- [ ] [TICKET-016-04] Write `test_list_view_excludes_draft_articles` test method
- [ ] [TICKET-016-05] Write `test_list_view_pagination` test method
- [ ] [TICKET-016-06] Write `test_list_view_filter_by_tag` test method
- [ ] [TICKET-016-07] Add `TestGeneratedArticleDetailView` test class
- [ ] [TICKET-016-08] Write `test_detail_view_displays_article` test method
- [ ] [TICKET-016-09] Write `test_detail_view_increments_view_count` test method
- [ ] [TICKET-016-10] Write `test_detail_view_shows_source_references` test method
- [ ] [TICKET-016-11] Write `test_detail_view_markdown_rendering` test method
- [ ] [TICKET-016-12] Add `TestGeneratedArticleFeed` test class
- [ ] [TICKET-016-13] Write `test_rss_feed_returns_articles` test method
- [ ] [TICKET-016-14] Write `test_rss_feed_validates` test method

#### Implementation Tasks - Template Tags
- [ ] [TICKET-016-15] Update `apps/content/templatetags/content_tags.py` to import markdown
- [ ] [TICKET-016-16] Create `render_markdown` filter
- [ ] [TICKET-016-17] Implement render_markdown to convert markdown to HTML
- [ ] [TICKET-016-18] Add safe HTML escaping to render_markdown
- [ ] [TICKET-016-19] Add support for code highlighting in render_markdown
- [ ] [TICKET-016-20] Add docstring to render_markdown filter

#### Implementation Tasks - Views
- [ ] [TICKET-016-21] Update `apps/content/views.py` to import GeneratedArticle
- [ ] [TICKET-016-22] Create `GeneratedArticleListView` class inheriting from ListView
- [ ] [TICKET-016-23] Set model = GeneratedArticle in GeneratedArticleListView
- [ ] [TICKET-016-24] Set template_name = 'content/generated_list.html'
- [ ] [TICKET-016-25] Set context_object_name = 'articles'
- [ ] [TICKET-016-26] Set paginate_by = 10
- [ ] [TICKET-016-27] Override get_queryset() to filter status='published'
- [ ] [TICKET-016-28] Order queryset by published_at descending
- [ ] [TICKET-016-29] Add tag filtering in get_queryset() from query params
- [ ] [TICKET-016-30] Override get_context_data() to add all unique tags
- [ ] [TICKET-016-31] Add selected_tag to context
- [ ] [TICKET-016-32] Create `GeneratedArticleDetailView` class inheriting from DetailView
- [ ] [TICKET-016-33] Set model = GeneratedArticle in GeneratedArticleDetailView
- [ ] [TICKET-016-34] Set template_name = 'content/generated_detail.html'
- [ ] [TICKET-016-35] Set context_object_name = 'article'
- [ ] [TICKET-016-36] Override get_queryset() to filter published articles
- [ ] [TICKET-016-37] Override get() method to increment view_count
- [ ] [TICKET-016-38] Use F() expression to avoid race conditions in view_count
- [ ] [TICKET-016-39] Override get_context_data() to add source_references
- [ ] [TICKET-016-40] Add related articles to context (same tags, limit 5)
- [ ] [TICKET-016-41] Add docstrings to views

#### Implementation Tasks - Templates
- [ ] [TICKET-016-42] Create `apps/content/templates/content/generated_list.html` extending base.html
- [ ] [TICKET-016-43] Add page title "AI-Generated Articles" to generated_list.html
- [ ] [TICKET-016-44] Create filter sidebar with tag list in generated_list.html
- [ ] [TICKET-016-45] Add "All" option to clear tag filter
- [ ] [TICKET-016-46] Create main content area with article cards loop
- [ ] [TICKET-016-47] Display title, excerpt, tags in each card
- [ ] [TICKET-016-48] Display published date and view count in each card
- [ ] [TICKET-016-49] Add link to detail view using slug
- [ ] [TICKET-016-50] Add pagination controls at bottom
- [ ] [TICKET-016-51] Add HTMX attributes for infinite scroll (optional)
- [ ] [TICKET-016-52] Create `apps/content/templates/content/generated_detail.html` extending base.html
- [ ] [TICKET-016-53] Add article title as page title
- [ ] [TICKET-016-54] Display article metadata (published date, view count, reading time)
- [ ] [TICKET-016-55] Render article body using render_markdown filter
- [ ] [TICKET-016-56] Create sidebar with metadata section
- [ ] [TICKET-016-57] Display generation info (model used, date generated) in sidebar
- [ ] [TICKET-016-58] Display tags with links to filtered list
- [ ] [TICKET-016-59] Create source references section in sidebar
- [ ] [TICKET-016-60] Loop through source_references and display links
- [ ] [TICKET-016-61] Create related articles section at bottom
- [ ] [TICKET-016-62] Display related article cards (title, excerpt, link)
- [ ] [TICKET-016-63] Add social sharing buttons (placeholder)
- [ ] [TICKET-016-64] Add SEO meta tags in <head> section
- [ ] [TICKET-016-65] Add meta description from article.meta_description
- [ ] [TICKET-016-66] Add Open Graph tags (og:title, og:description, og:type)
- [ ] [TICKET-016-67] Add Twitter Card tags (twitter:card, twitter:title, twitter:description)

#### Implementation Tasks - RSS Feed
- [ ] [TICKET-016-68] Create `apps/content/feeds.py` with imports
- [ ] [TICKET-016-69] Import Feed from django.contrib.syndication.views
- [ ] [TICKET-016-70] Create `GeneratedArticleFeed` class inheriting from Feed
- [ ] [TICKET-016-71] Set title = "Frugal Living - AI Generated Articles"
- [ ] [TICKET-016-72] Set link = "/generated/"
- [ ] [TICKET-016-73] Set description = "Latest AI-generated articles on frugal living"
- [ ] [TICKET-016-74] Implement items() method to return last 20 published articles
- [ ] [TICKET-016-75] Implement item_title() method returning article.title
- [ ] [TICKET-016-76] Implement item_description() method returning article.excerpt
- [ ] [TICKET-016-77] Implement item_link() method returning article detail URL
- [ ] [TICKET-016-78] Implement item_pubdate() method returning article.published_at
- [ ] [TICKET-016-79] Add docstring to GeneratedArticleFeed

#### Implementation Tasks - URLs
- [ ] [TICKET-016-80] Update `apps/content/urls.py` to import new views and feed
- [ ] [TICKET-016-81] Add URL pattern for GeneratedArticleListView (path 'generated/', name='generated_list')
- [ ] [TICKET-016-82] Add URL pattern for GeneratedArticleDetailView (path 'generated/<slug:slug>/', name='generated_detail')
- [ ] [TICKET-016-83] Add URL pattern for RSS feed (path 'feed/generated/', name='generated_feed')

#### Implementation Tasks - Navigation
- [ ] [TICKET-016-84] Update `templates/components/navbar.html` to add link to generated articles
- [ ] [TICKET-016-85] Add "AI Articles" menu item with URL to generated_list

#### Requirements Tasks
- [ ] [TICKET-016-86] Add markdown>=3.5 to `requirements/base.txt`
- [ ] [TICKET-016-87] Add pymdown-extensions>=10.0 to `requirements/base.txt` (for code highlighting)

#### Verification Tasks
- [ ] [TICKET-016-88] Run `pip install -r requirements/development.txt`
- [ ] [TICKET-016-89] Create test GeneratedArticle instances with status='published'
- [ ] [TICKET-016-90] Start development server
- [ ] [TICKET-016-91] Access generated articles list page and verify articles display
- [ ] [TICKET-016-92] Verify pagination works
- [ ] [TICKET-016-93] Test tag filtering by clicking on tags
- [ ] [TICKET-016-94] Click on article and verify detail page loads
- [ ] [TICKET-016-95] Verify markdown renders correctly
- [ ] [TICKET-016-96] Verify view count increments on page refresh
- [ ] [TICKET-016-97] Verify source references display with links
- [ ] [TICKET-016-98] Verify related articles section shows relevant articles
- [ ] [TICKET-016-99] Access RSS feed URL and verify XML validates
- [ ] [TICKET-016-100] Verify SEO meta tags in page source
- [ ] [TICKET-016-101] Test responsive design on mobile viewport
- [ ] [TICKET-016-102] Run `pytest apps/content/tests/test_generated_views.py -v`
- [ ] [TICKET-016-103] Verify all tests pass

---

### TICKET-017: Newsletter Model and Generation
**Dependencies:** TICKET-015

#### Test Tasks
- [ ] [TICKET-017-01] Create `apps/content/tests/test_newsletter.py` with imports
- [ ] [TICKET-017-02] Add `TestNewsletterModel` test class
- [ ] [TICKET-017-03] Write `test_newsletter_creation` test method
- [ ] [TICKET-017-04] Write `test_get_next_issue_number` test method
- [ ] [TICKET-017-05] Write `test_str_method` test method
- [ ] [TICKET-017-06] Write `test_included_articles_relationship` test method
- [ ] [TICKET-017-07] Add `TestNewsletterGenerator` test class
- [ ] [TICKET-017-08] Write `test_generate_weekly_newsletter` test method (mocked AI)
- [ ] [TICKET-017-09] Write `test_newsletter_includes_top_articles` test method
- [ ] [TICKET-017-10] Write `test_newsletter_html_generation` test method
- [ ] [TICKET-017-11] Write `test_newsletter_text_generation` test method
- [ ] [TICKET-017-12] Add `TestNewsletterTasks` test class
- [ ] [TICKET-017-13] Write `test_generate_weekly_newsletter_task` test method (mocked)

#### Implementation Tasks - Model
- [ ] [TICKET-017-14] Update `apps/content/models.py` to add Newsletter imports
- [ ] [TICKET-017-15] Create STATUS_CHOICES tuple for Newsletter
- [ ] [TICKET-017-16] Create `Newsletter` model class inheriting from TimeStampedModel
- [ ] [TICKET-017-17] Add `issue_number` field (IntegerField, unique=True, db_index=True)
- [ ] [TICKET-017-18] Add `issue_date` field (DateField, db_index=True)
- [ ] [TICKET-017-19] Add `subject` field (CharField, max_length=255)
- [ ] [TICKET-017-20] Add `html_body` field (TextField)
- [ ] [TICKET-017-21] Add `text_body` field (TextField)
- [ ] [TICKET-017-22] Add `included_articles` field (ManyToManyField to GeneratedArticle, related_name='newsletters')
- [ ] [TICKET-017-23] Add `included_resources` field (ManyToManyField to ProcessedContent, related_name='newsletters')
- [ ] [TICKET-017-24] Add `status` field (CharField with STATUS_CHOICES, default='draft', db_index=True)
- [ ] [TICKET-017-25] Add `scheduled_for` field (DateTimeField, null=True, blank=True)
- [ ] [TICKET-017-26] Add `sent_at` field (DateTimeField, null=True, blank=True)
- [ ] [TICKET-017-27] Add `recipient_count` field (IntegerField, default=0)
- [ ] [TICKET-017-28] Add `open_count` field (IntegerField, default=0)
- [ ] [TICKET-017-29] Add `click_count` field (IntegerField, default=0)
- [ ] [TICKET-017-30] Implement `__str__()` method returning issue number and date
- [ ] [TICKET-017-31] Implement `get_next_issue_number()` class method
- [ ] [TICKET-017-32] Query max issue_number and add 1 in get_next_issue_number()
- [ ] [TICKET-017-33] Handle case when no newsletters exist (return 1)
- [ ] [TICKET-017-34] Add Meta class with db_table = 'content_newsletter'
- [ ] [TICKET-017-35] Add ordering = ['-issue_number'] to Meta
- [ ] [TICKET-017-36] Add index on (status, scheduled_for) to Meta
- [ ] [TICKET-017-37] Add docstrings to Newsletter model and methods

#### Implementation Tasks - Email Templates
- [ ] [TICKET-017-38] Create `apps/content/templates/email/` directory
- [ ] [TICKET-017-39] Create `apps/content/templates/email/newsletter_base.html`
- [ ] [TICKET-017-40] Add HTML5 doctype and responsive meta tags to newsletter_base.html
- [ ] [TICKET-017-41] Add inline CSS for email compatibility
- [ ] [TICKET-017-42] Create header section with logo placeholder
- [ ] [TICKET-017-43] Create intro section with {% block intro %}
- [ ] [TICKET-017-44] Create articles section with {% block articles %}
- [ ] [TICKET-017-45] Create resources section with {% block resources %}
- [ ] [TICKET-017-46] Create footer with unsubscribe link placeholder
- [ ] [TICKET-017-47] Add social media links (placeholders) to footer
- [ ] [TICKET-017-48] Ensure table-based layout for email compatibility
- [ ] [TICKET-017-49] Create `apps/content/templates/email/newsletter_text.txt`
- [ ] [TICKET-017-50] Add plain text header to newsletter_text.txt
- [ ] [TICKET-017-51] Add {% block intro_text %} to newsletter_text.txt
- [ ] [TICKET-017-52] Add {% block articles_text %} to newsletter_text.txt
- [ ] [TICKET-017-53] Add {% block resources_text %} to newsletter_text.txt
- [ ] [TICKET-017-54] Add footer with unsubscribe link to newsletter_text.txt

#### Implementation Tasks - Services
- [ ] [TICKET-017-55] Update `apps/content/services.py` to add NewsletterGenerator imports
- [ ] [TICKET-017-56] Import Django template rendering utilities
- [ ] [TICKET-017-57] Create `NewsletterGenerator` class
- [ ] [TICKET-017-58] Add `__init__()` method to NewsletterGenerator
- [ ] [TICKET-017-59] Create `generate_weekly_newsletter()` method
- [ ] [TICKET-017-60] Calculate date range for past week in generate_weekly_newsletter()
- [ ] [TICKET-017-61] Fetch top 5 GeneratedArticles by view_count from past week
- [ ] [TICKET-017-62] Fetch top 10 ProcessedContent items by relevance
- [ ] [TICKET-017-63] Create context dictionary with articles and resources
- [ ] [TICKET-017-64] Generate intro/outro text using AIService
- [ ] [TICKET-017-65] Add intro text to context
- [ ] [TICKET-017-66] Render HTML template with context
- [ ] [TICKET-017-67] Render text template with context
- [ ] [TICKET-017-68] Get next issue number
- [ ] [TICKET-017-69] Create Newsletter instance with all data
- [ ] [TICKET-017-70] Add included_articles to newsletter
- [ ] [TICKET-017-71] Add included_resources to newsletter
- [ ] [TICKET-017-72] Save newsletter and return instance
- [ ] [TICKET-017-73] Add error handling and logging
- [ ] [TICKET-017-74] Add docstrings to NewsletterGenerator and methods

#### Implementation Tasks - Tasks
- [ ] [TICKET-017-75] Update `apps/content/tasks.py` to import NewsletterGenerator
- [ ] [TICKET-017-76] Create `generate_weekly_newsletter_task()` function with @shared_task
- [ ] [TICKET-017-77] Instantiate NewsletterGenerator in task
- [ ] [TICKET-017-78] Call generate_weekly_newsletter() method
- [ ] [TICKET-017-79] Log success with newsletter ID
- [ ] [TICKET-017-80] Handle exceptions and log errors
- [ ] [TICKET-017-81] Return newsletter ID or error status
- [ ] [TICKET-017-82] Add docstring to task

#### Implementation Tasks - Beat Schedule
- [ ] [TICKET-017-83] Update CELERY_BEAT_SCHEDULE in `config/settings/base.py`
- [ ] [TICKET-017-84] Add 'generate-weekly-newsletter' task entry
- [ ] [TICKET-017-85] Set schedule to crontab(day_of_week=1, hour=8, minute=0) for Monday 8 AM

#### Admin Tasks
- [ ] [TICKET-017-86] Update `apps/content/admin.py` to import Newsletter
- [ ] [TICKET-017-87] Create `NewsletterAdmin` class
- [ ] [TICKET-017-88] Add list_display (issue_number, issue_date, subject, status, recipient_count)
- [ ] [TICKET-017-89] Add list_filter (status, issue_date)
- [ ] [TICKET-017-90] Add search_fields (subject, html_body, text_body)
- [ ] [TICKET-017-91] Add readonly_fields (issue_number, sent_at, recipient_count, open_count, click_count)
- [ ] [TICKET-017-92] Add filter_horizontal for included_articles and included_resources
- [ ] [TICKET-017-93] Create custom admin view for HTML preview
- [ ] [TICKET-017-94] Add "Preview HTML" button to admin
- [ ] [TICKET-017-95] Create custom admin view for text preview
- [ ] [TICKET-017-96] Add "Preview Text" button to admin
- [ ] [TICKET-017-97] Create `schedule_newsletter` admin action
- [ ] [TICKET-017-98] Create `send_test_newsletter` admin action (placeholder)
- [ ] [TICKET-017-99] Add actions to NewsletterAdmin
- [ ] [TICKET-017-100] Register Newsletter with NewsletterAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-017-101] Run `python manage.py makemigrations content`
- [ ] [TICKET-017-102] Run `python manage.py migrate`
- [ ] [TICKET-017-103] Run `python manage.py check`
- [ ] [TICKET-017-104] Run `pytest apps/content/tests/test_newsletter.py -v`
- [ ] [TICKET-017-105] Verify all tests pass
- [ ] [TICKET-017-106] Create test GeneratedArticle and ProcessedContent instances
- [ ] [TICKET-017-107] Run generate_weekly_newsletter_task manually
- [ ] [TICKET-017-108] Verify Newsletter created in database
- [ ] [TICKET-017-109] Verify issue_number auto-increments
- [ ] [TICKET-017-110] Verify HTML and text bodies generated
- [ ] [TICKET-017-111] Open admin and preview HTML version
- [ ] [TICKET-017-112] Verify HTML renders correctly in browser
- [ ] [TICKET-017-113] Preview text version and verify formatting
- [ ] [TICKET-017-114] Verify Celery Beat schedule includes weekly newsletter task

---

### TICKET-018: Email Subscription Management
**Dependencies:** TICKET-017

#### Test Tasks
- [ ] [TICKET-018-01] Create `apps/subscribers/` directory
- [ ] [TICKET-018-02] Create `apps/subscribers/__init__.py`
- [ ] [TICKET-018-03] Create `apps/subscribers/tests/` directory
- [ ] [TICKET-018-04] Create `apps/subscribers/tests/__init__.py`
- [ ] [TICKET-018-05] Create `apps/subscribers/tests/test_models.py` with imports
- [ ] [TICKET-018-06] Add `TestSubscriberModel` test class
- [ ] [TICKET-018-07] Write `test_subscriber_creation` test method
- [ ] [TICKET-018-08] Write `test_generate_confirmation_token` test method
- [ ] [TICKET-018-09] Write `test_confirm_method` test method
- [ ] [TICKET-018-10] Write `test_unsubscribe_method` test method
- [ ] [TICKET-018-11] Write `test_str_method` test method
- [ ] [TICKET-018-12] Create `apps/subscribers/tests/test_views.py` with imports
- [ ] [TICKET-018-13] Add `TestSubscriptionViews` test class
- [ ] [TICKET-018-14] Write `test_subscribe_view_get` test method
- [ ] [TICKET-018-15] Write `test_subscribe_view_post_valid` test method
- [ ] [TICKET-018-16] Write `test_subscribe_view_post_duplicate` test method
- [ ] [TICKET-018-17] Write `test_confirm_subscription_view` test method
- [ ] [TICKET-018-18] Write `test_unsubscribe_view` test method
- [ ] [TICKET-018-19] Create `apps/subscribers/tests/test_tasks.py` with imports
- [ ] [TICKET-018-20] Write `test_send_confirmation_email` test method (mocked)
- [ ] [TICKET-018-21] Write `test_send_newsletter_to_subscribers` test method (mocked)

#### Implementation Tasks - Apps Config
- [ ] [TICKET-018-22] Create `apps/subscribers/apps.py` with SubscribersConfig class
- [ ] [TICKET-018-23] Set name = 'apps.subscribers' in SubscribersConfig
- [ ] [TICKET-018-24] Add 'apps.subscribers' to INSTALLED_APPS in `config/settings/base.py`

#### Implementation Tasks - Model
- [ ] [TICKET-018-25] Create `apps/subscribers/models.py` with imports
- [ ] [TICKET-018-26] Import secrets for token generation
- [ ] [TICKET-018-27] Create `Subscriber` model class inheriting from TimeStampedModel
- [ ] [TICKET-018-28] Add `email` field (EmailField, unique=True, db_index=True)
- [ ] [TICKET-018-29] Add `first_name` field (CharField, max_length=100, blank=True, default='')
- [ ] [TICKET-018-30] Add `is_active` field (BooleanField, default=True, db_index=True)
- [ ] [TICKET-018-31] Add `subscribed_at` field (DateTimeField, auto_now_add=True)
- [ ] [TICKET-018-32] Add `unsubscribed_at` field (DateTimeField, null=True, blank=True)
- [ ] [TICKET-018-33] Add `confirmation_token` field (CharField, max_length=64, unique=True, db_index=True)
- [ ] [TICKET-018-34] Add `is_confirmed` field (BooleanField, default=False, db_index=True)
- [ ] [TICKET-018-35] Add `confirmed_at` field (DateTimeField, null=True, blank=True)
- [ ] [TICKET-018-36] Add `preferences` field (JSONField, default=dict, blank=True)
- [ ] [TICKET-018-37] Implement `generate_confirmation_token()` method using secrets.token_urlsafe()
- [ ] [TICKET-018-38] Implement `confirm()` method to set is_confirmed=True and confirmed_at
- [ ] [TICKET-018-39] Implement `unsubscribe()` method to set is_active=False and unsubscribed_at
- [ ] [TICKET-018-40] Implement `__str__()` method returning email
- [ ] [TICKET-018-41] Override `save()` to auto-generate confirmation_token if not set
- [ ] [TICKET-018-42] Add Meta class with db_table = 'subscribers_subscriber'
- [ ] [TICKET-018-43] Add ordering = ['-subscribed_at'] to Meta
- [ ] [TICKET-018-44] Add index on (is_active, is_confirmed) to Meta
- [ ] [TICKET-018-45] Add docstrings to Subscriber model and methods

#### Implementation Tasks - Forms
- [ ] [TICKET-018-46] Create `apps/subscribers/forms.py` with imports
- [ ] [TICKET-018-47] Create `SubscribeForm` class inheriting from forms.Form
- [ ] [TICKET-018-48] Add `email` field (EmailField with validators)
- [ ] [TICKET-018-49] Add `first_name` field (CharField, max_length=100, required=False)
- [ ] [TICKET-018-50] Implement `clean_email()` to check for existing active subscribers
- [ ] [TICKET-018-51] Add helpful error message for duplicate emails
- [ ] [TICKET-018-52] Add docstring to SubscribeForm

#### Implementation Tasks - Views
- [ ] [TICKET-018-53] Create `apps/subscribers/views.py` with imports
- [ ] [TICKET-018-54] Create `SubscribeView` class inheriting from FormView
- [ ] [TICKET-018-55] Set template_name = 'subscribers/subscribe.html'
- [ ] [TICKET-018-56] Set form_class = SubscribeForm
- [ ] [TICKET-018-57] Set success_url to reverse_lazy('subscribers:success')
- [ ] [TICKET-018-58] Override form_valid() to create Subscriber instance
- [ ] [TICKET-018-59] Dispatch send_confirmation_email task in form_valid()
- [ ] [TICKET-018-60] Add success message in form_valid()
- [ ] [TICKET-018-61] Create `ConfirmSubscriptionView` class inheriting from View
- [ ] [TICKET-018-62] Set template_name = 'subscribers/confirm.html'
- [ ] [TICKET-018-63] Implement get() method to fetch subscriber by token
- [ ] [TICKET-018-64] Call subscriber.confirm() if valid token
- [ ] [TICKET-018-65] Render success or error message
- [ ] [TICKET-018-66] Create `UnsubscribeView` class inheriting from View
- [ ] [TICKET-018-67] Set template_name = 'subscribers/unsubscribe.html'
- [ ] [TICKET-018-68] Implement get() method to fetch subscriber by token
- [ ] [TICKET-018-69] Call subscriber.unsubscribe() if valid token
- [ ] [TICKET-018-70] Render success or error message
- [ ] [TICKET-018-71] Create `SubscriptionSuccessView` class inheriting from TemplateView
- [ ] [TICKET-018-72] Set template_name = 'subscribers/success.html'
- [ ] [TICKET-018-73] Add docstrings to all views

#### Implementation Tasks - Templates
- [ ] [TICKET-018-74] Create `apps/subscribers/templates/` directory
- [ ] [TICKET-018-75] Create `apps/subscribers/templates/subscribers/` directory
- [ ] [TICKET-018-76] Create `apps/subscribers/templates/subscribers/subscribe.html` extending base.html
- [ ] [TICKET-018-77] Add subscription form with email and first_name fields
- [ ] [TICKET-018-78] Add CSRF token to form
- [ ] [TICKET-018-79] Add submit button with clear CTA
- [ ] [TICKET-018-80] Add privacy notice about email usage
- [ ] [TICKET-018-81] Create `apps/subscribers/templates/subscribers/success.html` extending base.html
- [ ] [TICKET-018-82] Add success message about confirmation email
- [ ] [TICKET-018-83] Create `apps/subscribers/templates/subscribers/confirm.html` extending base.html
- [ ] [TICKET-018-84] Add confirmation success/error message
- [ ] [TICKET-018-85] Create `apps/subscribers/templates/subscribers/unsubscribe.html` extending base.html
- [ ] [TICKET-018-86] Add unsubscribe confirmation message
- [ ] [TICKET-018-87] Create `apps/subscribers/templates/email/` directory
- [ ] [TICKET-018-88] Create `apps/subscribers/templates/email/confirmation.html`
- [ ] [TICKET-018-89] Add confirmation email HTML with personalized greeting
- [ ] [TICKET-018-90] Add confirmation link with token
- [ ] [TICKET-018-91] Add welcome message and what to expect
- [ ] [TICKET-018-92] Create `apps/subscribers/templates/email/confirmation.txt` (plain text version)

#### Implementation Tasks - Tasks
- [ ] [TICKET-018-93] Create `apps/subscribers/tasks.py` with imports
- [ ] [TICKET-018-94] Create `send_confirmation_email(subscriber_id)` function with @shared_task
- [ ] [TICKET-018-95] Fetch Subscriber by ID in task
- [ ] [TICKET-018-96] Build confirmation URL with token
- [ ] [TICKET-018-97] Render HTML email template with context
- [ ] [TICKET-018-98] Render text email template with context
- [ ] [TICKET-018-99] Send email using Django's send_mail()
- [ ] [TICKET-018-100] Log success or errors
- [ ] [TICKET-018-101] Create `send_newsletter_to_subscribers(newsletter_id)` function with @shared_task
- [ ] [TICKET-018-102] Fetch Newsletter by ID
- [ ] [TICKET-018-103] Query active, confirmed subscribers
- [ ] [TICKET-018-104] Loop through subscribers and send newsletter
- [ ] [TICKET-018-105] Add unsubscribe link to each email
- [ ] [TICKET-018-106] Update Newsletter.recipient_count
- [ ] [TICKET-018-107] Update Newsletter.status to 'sent'
- [ ] [TICKET-018-108] Update Newsletter.sent_at timestamp
- [ ] [TICKET-018-109] Add error handling and logging
- [ ] [TICKET-018-110] Add docstrings to tasks

#### Implementation Tasks - URLs
- [ ] [TICKET-018-111] Create `apps/subscribers/urls.py` with imports
- [ ] [TICKET-018-112] Set app_name = 'subscribers'
- [ ] [TICKET-018-113] Add URL pattern for SubscribeView (path 'subscribe/', name='subscribe')
- [ ] [TICKET-018-114] Add URL pattern for ConfirmSubscriptionView (path 'confirm/<str:token>/', name='confirm')
- [ ] [TICKET-018-115] Add URL pattern for UnsubscribeView (path 'unsubscribe/<str:token>/', name='unsubscribe')
- [ ] [TICKET-018-116] Add URL pattern for SubscriptionSuccessView (path 'success/', name='success')
- [ ] [TICKET-018-117] Update `config/urls.py` to include subscribers.urls at 'newsletter/'

#### Settings Tasks
- [ ] [TICKET-018-118] Add EMAIL_BACKEND to `config/settings/development.py` (console backend)
- [ ] [TICKET-018-119] Add EMAIL_BACKEND to `config/settings/production.py` (SMTP backend)
- [ ] [TICKET-018-120] Add EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS to production.py from environment
- [ ] [TICKET-018-121] Add EMAIL_HOST_USER, EMAIL_HOST_PASSWORD to production.py from environment
- [ ] [TICKET-018-122] Add DEFAULT_FROM_EMAIL to base.py
- [ ] [TICKET-018-123] Update `.env.example` with email settings

#### Admin Tasks
- [ ] [TICKET-018-124] Create `apps/subscribers/admin.py` with imports
- [ ] [TICKET-018-125] Create `SubscriberAdmin` class
- [ ] [TICKET-018-126] Add list_display (email, first_name, is_active, is_confirmed, subscribed_at)
- [ ] [TICKET-018-127] Add list_filter (is_active, is_confirmed, subscribed_at)
- [ ] [TICKET-018-128] Add search_fields (email, first_name)
- [ ] [TICKET-018-129] Add readonly_fields (confirmation_token, subscribed_at, confirmed_at, unsubscribed_at)
- [ ] [TICKET-018-130] Create `export_emails` admin action
- [ ] [TICKET-018-131] Implement export_emails to return CSV of active subscribers
- [ ] [TICKET-018-132] Add actions to SubscriberAdmin
- [ ] [TICKET-018-133] Register Subscriber with SubscriberAdmin

#### Navigation Tasks
- [ ] [TICKET-018-134] Update `templates/base.html` to add newsletter signup link in footer
- [ ] [TICKET-018-135] Add link to subscribers:subscribe

#### Migration and Verification Tasks
- [ ] [TICKET-018-136] Run `python manage.py makemigrations subscribers`
- [ ] [TICKET-018-137] Run `python manage.py migrate`
- [ ] [TICKET-018-138] Run `python manage.py check`
- [ ] [TICKET-018-139] Run `pytest apps/subscribers/tests/ -v`
- [ ] [TICKET-018-140] Verify all tests pass
- [ ] [TICKET-018-141] Access subscribe page and submit form
- [ ] [TICKET-018-142] Verify Subscriber created in database
- [ ] [TICKET-018-143] Check console for confirmation email (development)
- [ ] [TICKET-018-144] Copy confirmation link and access it
- [ ] [TICKET-018-145] Verify subscriber confirmed in database
- [ ] [TICKET-018-146] Test unsubscribe link
- [ ] [TICKET-018-147] Verify subscriber marked inactive
- [ ] [TICKET-018-148] Test duplicate email submission
- [ ] [TICKET-018-149] Verify appropriate error message shown
- [ ] [TICKET-018-150] Test send_newsletter_to_subscribers task with test newsletter

---

## PHASE 3: COMMUNITY FORUM MVP

### TICKET-019: Users App - User Profile Model
**Dependencies:** TICKET-001

#### Test Tasks
- [ ] [TICKET-019-01] Create `apps/users/` directory
- [ ] [TICKET-019-02] Create `apps/users/__init__.py`
- [ ] [TICKET-019-03] Create `apps/users/tests/` directory
- [ ] [TICKET-019-04] Create `apps/users/tests/__init__.py`
- [ ] [TICKET-019-05] Create `apps/users/tests/test_models.py` with imports
- [ ] [TICKET-019-06] Add `TestUserProfileModel` test class
- [ ] [TICKET-019-07] Write `test_user_profile_creation` test method
- [ ] [TICKET-019-08] Write `test_user_profile_auto_created_on_user_save` test method
- [ ] [TICKET-019-09] Write `test_get_avatar_url_with_avatar` test method
- [ ] [TICKET-019-10] Write `test_get_avatar_url_without_avatar` test method
- [ ] [TICKET-019-11] Write `test_str_method` test method
- [ ] [TICKET-019-12] Create `apps/users/tests/test_views.py` with imports
- [ ] [TICKET-019-13] Add `TestRegistrationView` test class
- [ ] [TICKET-019-14] Write `test_register_view_get` test method
- [ ] [TICKET-019-15] Write `test_register_view_post_valid` test method
- [ ] [TICKET-019-16] Write `test_register_view_post_invalid` test method
- [ ] [TICKET-019-17] Add `TestProfileViews` test class
- [ ] [TICKET-019-18] Write `test_profile_view` test method
- [ ] [TICKET-019-19] Write `test_profile_edit_view` test method

#### Implementation Tasks - Apps Config
- [ ] [TICKET-019-20] Create `apps/users/apps.py` with UsersConfig class
- [ ] [TICKET-019-21] Set name = 'apps.users' in UsersConfig
- [ ] [TICKET-019-22] Override ready() method to import signals
- [ ] [TICKET-019-23] Add 'apps.users' to INSTALLED_APPS in `config/settings/base.py`

#### Implementation Tasks - Model
- [ ] [TICKET-019-24] Create `apps/users/models.py` with imports
- [ ] [TICKET-019-25] Import User from django.contrib.auth.models
- [ ] [TICKET-019-26] Create `UserProfile` model class inheriting from TimeStampedModel
- [ ] [TICKET-019-27] Add `user` field (OneToOneField to User, on_delete=CASCADE, related_name='profile')
- [ ] [TICKET-019-28] Add `bio` field (TextField, max_length=500, blank=True, default='')
- [ ] [TICKET-019-29] Add `avatar` field (ImageField, upload_to='avatars/', null=True, blank=True)
- [ ] [TICKET-019-30] Add `location` field (CharField, max_length=100, blank=True, default='')
- [ ] [TICKET-019-31] Add `website` field (URLField, blank=True, default='')
- [ ] [TICKET-019-32] Add `forum_post_count` field (IntegerField, default=0)
- [ ] [TICKET-019-33] Add `forum_reputation` field (IntegerField, default=0)
- [ ] [TICKET-019-34] Add `interests` field (ArrayField of CharField, default=list, blank=True)
- [ ] [TICKET-019-35] Add `email_notifications` field (BooleanField, default=True)
- [ ] [TICKET-019-36] Implement `__str__()` method returning user.username
- [ ] [TICKET-019-37] Implement `get_avatar_url()` method
- [ ] [TICKET-019-38] Return avatar.url if avatar exists in get_avatar_url()
- [ ] [TICKET-019-39] Return default avatar URL if no avatar in get_avatar_url()
- [ ] [TICKET-019-40] Add Meta class with db_table = 'users_profile'
- [ ] [TICKET-019-41] Add ordering = ['-created_at'] to Meta
- [ ] [TICKET-019-42] Add docstrings to UserProfile model and methods

#### Implementation Tasks - Signals
- [ ] [TICKET-019-43] Create `apps/users/signals.py` with imports
- [ ] [TICKET-019-44] Import post_save signal and receiver decorator
- [ ] [TICKET-019-45] Create `create_user_profile` function with @receiver decorator
- [ ] [TICKET-019-46] Connect to User post_save signal
- [ ] [TICKET-019-47] Check if instance is newly created
- [ ] [TICKET-019-48] Create UserProfile instance for new user
- [ ] [TICKET-019-49] Add docstring to signal handler

#### Implementation Tasks - Forms
- [ ] [TICKET-019-50] Create `apps/users/forms.py` with imports
- [ ] [TICKET-019-51] Import UserCreationForm from django.contrib.auth.forms
- [ ] [TICKET-019-52] Create `UserRegistrationForm` class inheriting from UserCreationForm
- [ ] [TICKET-019-53] Add email field to UserRegistrationForm
- [ ] [TICKET-019-54] Add first_name and last_name fields
- [ ] [TICKET-019-55] Add Meta class with User model and fields
- [ ] [TICKET-019-56] Implement clean_email() to check for duplicate emails
- [ ] [TICKET-019-57] Create `UserProfileForm` class inheriting from forms.ModelForm
- [ ] [TICKET-019-58] Add Meta class with UserProfile model
- [ ] [TICKET-019-59] Set fields = ['bio', 'avatar', 'location', 'website', 'interests']
- [ ] [TICKET-019-60] Add widgets for better UX (Textarea for bio)
- [ ] [TICKET-019-61] Create `UserSettingsForm` class inheriting from forms.ModelForm
- [ ] [TICKET-019-62] Add Meta class with UserProfile model
- [ ] [TICKET-019-63] Set fields = ['email_notifications']
- [ ] [TICKET-019-64] Add docstrings to all forms

#### Implementation Tasks - Views
- [ ] [TICKET-019-65] Create `apps/users/views.py` with imports
- [ ] [TICKET-019-66] Create `RegisterView` class inheriting from CreateView
- [ ] [TICKET-019-67] Set template_name = 'users/register.html'
- [ ] [TICKET-019-68] Set form_class = UserRegistrationForm
- [ ] [TICKET-019-69] Set success_url to reverse_lazy('login')
- [ ] [TICKET-019-70] Override form_valid() to add success message
- [ ] [TICKET-019-71] Create `ProfileView` class inheriting from DetailView
- [ ] [TICKET-019-72] Set model = User
- [ ] [TICKET-019-73] Set template_name = 'users/profile.html'
- [ ] [TICKET-019-74] Set context_object_name = 'profile_user'
- [ ] [TICKET-019-75] Override get_object() to fetch by username from URL
- [ ] [TICKET-019-76] Add profile and recent posts to context
- [ ] [TICKET-019-77] Create `ProfileEditView` class inheriting from UpdateView
- [ ] [TICKET-019-78] Set model = UserProfile
- [ ] [TICKET-019-79] Set template_name = 'users/profile_edit.html'
- [ ] [TICKET-019-80] Set form_class = UserProfileForm
- [ ] [TICKET-019-81] Add LoginRequiredMixin
- [ ] [TICKET-019-82] Override get_object() to return request.user.profile
- [ ] [TICKET-019-83] Set success_url to profile page
- [ ] [TICKET-019-84] Create `SettingsView` class inheriting from UpdateView
- [ ] [TICKET-019-85] Set model = UserProfile
- [ ] [TICKET-019-86] Set template_name = 'users/settings.html'
- [ ] [TICKET-019-87] Set form_class = UserSettingsForm
- [ ] [TICKET-019-88] Add LoginRequiredMixin
- [ ] [TICKET-019-89] Override get_object() to return request.user.profile
- [ ] [TICKET-019-90] Add docstrings to all views

#### Implementation Tasks - Templates
- [ ] [TICKET-019-91] Create `apps/users/templates/` directory
- [ ] [TICKET-019-92] Create `apps/users/templates/users/` directory
- [ ] [TICKET-019-93] Create `apps/users/templates/users/register.html` extending base.html
- [ ] [TICKET-019-94] Add registration form with all fields
- [ ] [TICKET-019-95] Add CSRF token and submit button
- [ ] [TICKET-019-96] Add link to login page for existing users
- [ ] [TICKET-019-97] Create `apps/users/templates/users/login.html` extending base.html
- [ ] [TICKET-019-98] Add Django's built-in login form
- [ ] [TICKET-019-99] Add link to registration page
- [ ] [TICKET-019-100] Create `apps/users/templates/users/profile.html` extending base.html
- [ ] [TICKET-019-101] Display user avatar, username, bio
- [ ] [TICKET-019-102] Display location, website if available
- [ ] [TICKET-019-103] Display forum stats (post count, reputation)
- [ ] [TICKET-019-104] Add "Edit Profile" button if viewing own profile
- [ ] [TICKET-019-105] Display recent forum posts
- [ ] [TICKET-019-106] Create `apps/users/templates/users/profile_edit.html` extending base.html
- [ ] [TICKET-019-107] Add profile edit form with all fields
- [ ] [TICKET-019-108] Add file upload widget for avatar
- [ ] [TICKET-019-109] Add CSRF token and submit button
- [ ] [TICKET-019-110] Create `apps/users/templates/users/settings.html` extending base.html
- [ ] [TICKET-019-111] Add settings form with email_notifications
- [ ] [TICKET-019-112] Add CSRF token and submit button

#### Implementation Tasks - URLs
- [ ] [TICKET-019-113] Create `apps/users/urls.py` with imports
- [ ] [TICKET-019-114] Set app_name = 'users'
- [ ] [TICKET-019-115] Add URL pattern for RegisterView (path 'register/', name='register')
- [ ] [TICKET-019-116] Add URL pattern for Django's LoginView (path 'login/', name='login')
- [ ] [TICKET-019-117] Add URL pattern for Django's LogoutView (path 'logout/', name='logout')
- [ ] [TICKET-019-118] Add URL pattern for ProfileView (path 'profile/<str:username>/', name='profile')
- [ ] [TICKET-019-119] Add URL pattern for ProfileEditView (path 'profile/edit/', name='profile_edit')
- [ ] [TICKET-019-120] Add URL pattern for SettingsView (path 'settings/', name='settings')
- [ ] [TICKET-019-121] Update `config/urls.py` to include users.urls at 'users/'

#### Settings Tasks
- [ ] [TICKET-019-122] Add LOGIN_URL = '/users/login/' to `config/settings/base.py`
- [ ] [TICKET-019-123] Add LOGIN_REDIRECT_URL = '/' to base.py
- [ ] [TICKET-019-124] Add LOGOUT_REDIRECT_URL = '/' to base.py
- [ ] [TICKET-019-125] Add AUTH_PASSWORD_VALIDATORS to base.py
- [ ] [TICKET-019-126] Configure MEDIA_URL = '/media/' in base.py
- [ ] [TICKET-019-127] Configure MEDIA_ROOT = BASE_DIR / 'media' in base.py

#### Requirements Tasks
- [ ] [TICKET-019-128] Add Pillow>=10.0 to `requirements/base.txt`

#### Admin Tasks
- [ ] [TICKET-019-129] Create `apps/users/admin.py` with imports
- [ ] [TICKET-019-130] Create `UserProfileAdmin` class
- [ ] [TICKET-019-131] Add list_display (user, location, forum_post_count, forum_reputation)
- [ ] [TICKET-019-132] Add list_filter (email_notifications, created_at)
- [ ] [TICKET-019-133] Add search_fields (user__username, user__email, location)
- [ ] [TICKET-019-134] Add readonly_fields (forum_post_count, forum_reputation, created_at)
- [ ] [TICKET-019-135] Register UserProfile with UserProfileAdmin

#### Navigation Tasks
- [ ] [TICKET-019-136] Update `templates/components/navbar.html` to add user menu
- [ ] [TICKET-019-137] Show "Login" and "Register" links if not authenticated
- [ ] [TICKET-019-138] Show username and dropdown menu if authenticated
- [ ] [TICKET-019-139] Add "Profile", "Settings", "Logout" links to dropdown

#### Migration and Verification Tasks
- [ ] [TICKET-019-140] Run `pip install -r requirements/development.txt`
- [ ] [TICKET-019-141] Run `python manage.py makemigrations users`
- [ ] [TICKET-019-142] Run `python manage.py migrate`
- [ ] [TICKET-019-143] Run `python manage.py check`
- [ ] [TICKET-019-144] Run `pytest apps/users/tests/ -v`
- [ ] [TICKET-019-145] Verify all tests pass
- [ ] [TICKET-019-146] Access registration page and create test user
- [ ] [TICKET-019-147] Verify UserProfile auto-created in database
- [ ] [TICKET-019-148] Login with test user
- [ ] [TICKET-019-149] Access profile page and verify data displays
- [ ] [TICKET-019-150] Edit profile and upload avatar
- [ ] [TICKET-019-151] Verify avatar saved and displays correctly
- [ ] [TICKET-019-152] Test settings page and email notifications toggle
- [ ] [TICKET-019-153] Logout and verify redirect
- [ ] [TICKET-019-154] Test login with created user

---

### TICKET-020: Forum App - Category and Topic Models
**Dependencies:** TICKET-019

#### Test Tasks
- [ ] [TICKET-020-01] Create `apps/forum/` directory
- [ ] [TICKET-020-02] Create `apps/forum/__init__.py`
- [ ] [TICKET-020-03] Create `apps/forum/tests/` directory
- [ ] [TICKET-020-04] Create `apps/forum/tests/__init__.py`
- [ ] [TICKET-020-05] Create `apps/forum/tests/factories.py` with ForumCategoryFactory
- [ ] [TICKET-020-06] Add ForumTopicFactory to factories.py
- [ ] [TICKET-020-07] Create `apps/forum/tests/test_models.py` with imports
- [ ] [TICKET-020-08] Add `TestForumCategoryModel` test class
- [ ] [TICKET-020-09] Write `test_category_creation` test method
- [ ] [TICKET-020-10] Write `test_category_slug_auto_generation` test method
- [ ] [TICKET-020-11] Write `test_update_counts` test method
- [ ] [TICKET-020-12] Write `test_str_method` test method
- [ ] [TICKET-020-13] Add `TestForumTopicModel` test class
- [ ] [TICKET-020-14] Write `test_topic_creation` test method
- [ ] [TICKET-020-15] Write `test_topic_slug_auto_generation` test method
- [ ] [TICKET-020-16] Write `test_update_last_post` test method
- [ ] [TICKET-020-17] Write `test_increment_view_count` test method
- [ ] [TICKET-020-18] Write `test_topic_ordering` test method (pinned first)

#### Implementation Tasks - Apps Config
- [ ] [TICKET-020-19] Create `apps/forum/apps.py` with ForumConfig class
- [ ] [TICKET-020-20] Set name = 'apps.forum' in ForumConfig
- [ ] [TICKET-020-21] Add 'apps.forum' to INSTALLED_APPS in `config/settings/base.py`

#### Implementation Tasks - Managers
- [ ] [TICKET-020-22] Create `apps/forum/managers.py` with imports
- [ ] [TICKET-020-23] Create `ForumTopicManager` class inheriting from models.Manager
- [ ] [TICKET-020-24] Implement `active()` method returning non-locked topics
- [ ] [TICKET-020-25] Implement `pinned()` method returning pinned topics
- [ ] [TICKET-020-26] Implement `recent()` method returning recently active topics
- [ ] [TICKET-020-27] Add docstrings to ForumTopicManager and methods

#### Implementation Tasks - Models
- [ ] [TICKET-020-28] Create `apps/forum/models.py` with imports
- [ ] [TICKET-020-29] Import User, slugify, timezone
- [ ] [TICKET-020-30] Create `ForumCategory` model class inheriting from models.Model
- [ ] [TICKET-020-31] Add `name` field (CharField, max_length=100, unique=True)
- [ ] [TICKET-020-32] Add `slug` field (SlugField, unique=True, db_index=True, max_length=110)
- [ ] [TICKET-020-33] Add `description` field (TextField, max_length=500)
- [ ] [TICKET-020-34] Add `order` field (IntegerField, default=0)
- [ ] [TICKET-020-35] Add `is_active` field (BooleanField, default=True, db_index=True)
- [ ] [TICKET-020-36] Add `topic_count` field (IntegerField, default=0)
- [ ] [TICKET-020-37] Add `post_count` field (IntegerField, default=0)
- [ ] [TICKET-020-38] Add `created_at` field (DateTimeField, auto_now_add=True)
- [ ] [TICKET-020-39] Override `save()` method to auto-generate slug from name
- [ ] [TICKET-020-40] Implement `update_counts()` method
- [ ] [TICKET-020-41] Query and count topics in update_counts()
- [ ] [TICKET-020-42] Query and count posts in update_counts()
- [ ] [TICKET-020-43] Save updated counts
- [ ] [TICKET-020-44] Implement `__str__()` method returning name
- [ ] [TICKET-020-45] Add Meta class with db_table = 'forum_category'
- [ ] [TICKET-020-46] Add ordering = ['order', 'name'] to Meta
- [ ] [TICKET-020-47] Add docstrings to ForumCategory model and methods
- [ ] [TICKET-020-48] Create `ForumTopic` model class inheriting from models.Model
- [ ] [TICKET-020-49] Add `category` field (ForeignKey to ForumCategory, on_delete=CASCADE, related_name='topics')
- [ ] [TICKET-020-50] Add `title` field (CharField, max_length=255)
- [ ] [TICKET-020-51] Add `slug` field (SlugField, max_length=300, db_index=True)
- [ ] [TICKET-020-52] Add `creator` field (ForeignKey to User, on_delete=CASCADE, related_name='forum_topics')
- [ ] [TICKET-020-53] Add `is_pinned` field (BooleanField, default=False, db_index=True)
- [ ] [TICKET-020-54] Add `is_locked` field (BooleanField, default=False)
- [ ] [TICKET-020-55] Add `view_count` field (IntegerField, default=0)
- [ ] [TICKET-020-56] Add `post_count` field (IntegerField, default=0)
- [ ] [TICKET-020-57] Add `created_at` field (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-020-58] Add `updated_at` field (DateTimeField, auto_now=True)
- [ ] [TICKET-020-59] Add `last_post_at` field (DateTimeField, null=True, blank=True, db_index=True)
- [ ] [TICKET-020-60] Add `last_post_by` field (ForeignKey to User, null=True, on_delete=SET_NULL, related_name='+')
- [ ] [TICKET-020-61] Set objects = ForumTopicManager()
- [ ] [TICKET-020-62] Override `save()` method to auto-generate slug from title
- [ ] [TICKET-020-63] Add slug uniqueness handling in save()
- [ ] [TICKET-020-64] Implement `update_last_post(post)` method
- [ ] [TICKET-020-65] Set last_post_at to post.created_at
- [ ] [TICKET-020-66] Set last_post_by to post.author
- [ ] [TICKET-020-67] Save topic
- [ ] [TICKET-020-68] Implement `increment_view_count()` method using F() expression
- [ ] [TICKET-020-69] Implement `__str__()` method returning title
- [ ] [TICKET-020-70] Add Meta class with db_table = 'forum_topic'
- [ ] [TICKET-020-71] Add ordering = ['-is_pinned', '-last_post_at'] to Meta
- [ ] [TICKET-020-72] Add composite index on (category, is_pinned, last_post_at) to Meta
- [ ] [TICKET-020-73] Add unique_together on (category, slug) to Meta
- [ ] [TICKET-020-74] Add docstrings to ForumTopic model and methods

#### Admin Tasks
- [ ] [TICKET-020-75] Create `apps/forum/admin.py` with imports
- [ ] [TICKET-020-76] Create `ForumCategoryAdmin` class
- [ ] [TICKET-020-77] Add list_display (name, order, topic_count, post_count, is_active)
- [ ] [TICKET-020-78] Add list_filter (is_active, created_at)
- [ ] [TICKET-020-79] Add search_fields (name, description)
- [ ] [TICKET-020-80] Add readonly_fields (slug, topic_count, post_count, created_at)
- [ ] [TICKET-020-81] Add ordering by order field
- [ ] [TICKET-020-82] Register ForumCategory with ForumCategoryAdmin
- [ ] [TICKET-020-83] Create `ForumTopicAdmin` class
- [ ] [TICKET-020-84] Add list_display (title, category, creator, is_pinned, is_locked, post_count, view_count)
- [ ] [TICKET-020-85] Add list_filter (category, is_pinned, is_locked, created_at)
- [ ] [TICKET-020-86] Add search_fields (title, creator__username)
- [ ] [TICKET-020-87] Add readonly_fields (slug, view_count, post_count, created_at, last_post_at)
- [ ] [TICKET-020-88] Register ForumTopic with ForumTopicAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-020-89] Run `python manage.py makemigrations forum`
- [ ] [TICKET-020-90] Run `python manage.py migrate`
- [ ] [TICKET-020-91] Run `python manage.py check`
- [ ] [TICKET-020-92] Run `pytest apps/forum/tests/test_models.py -v`
- [ ] [TICKET-020-93] Verify all tests pass
- [ ] [TICKET-020-94] Create test ForumCategory in admin
- [ ] [TICKET-020-95] Verify slug auto-generated
- [ ] [TICKET-020-96] Create test ForumTopic in admin
- [ ] [TICKET-020-97] Verify slug auto-generated
- [ ] [TICKET-020-98] Test update_counts() method manually
- [ ] [TICKET-020-99] Test increment_view_count() method manually

---

### TICKET-021: Forum App - Post Model and Moderation
**Dependencies:** TICKET-020

#### Test Tasks
- [ ] [TICKET-021-01] Add ForumPostFactory to `apps/forum/tests/factories.py`
- [ ] [TICKET-021-02] Create `apps/forum/tests/test_posts.py` with imports
- [ ] [TICKET-021-03] Add `TestForumPostModel` test class
- [ ] [TICKET-021-04] Write `test_post_creation` test method
- [ ] [TICKET-021-05] Write `test_mark_as_edited` test method
- [ ] [TICKET-021-06] Write `test_soft_delete` test method
- [ ] [TICKET-021-07] Write `test_str_method` test method
- [ ] [TICKET-021-08] Add `TestForumPostSignals` test class
- [ ] [TICKET-021-09] Write `test_post_creation_updates_topic_count` test method
- [ ] [TICKET-021-10] Write `test_post_creation_updates_category_count` test method
- [ ] [TICKET-021-11] Write `test_post_creation_updates_user_profile` test method
- [ ] [TICKET-021-12] Write `test_post_creation_updates_last_post` test method
- [ ] [TICKET-021-13] Add `TestForumPostManager` test class
- [ ] [TICKET-021-14] Write `test_approved_manager_method` test method
- [ ] [TICKET-021-15] Write `test_visible_manager_method` test method
- [ ] [TICKET-021-16] Write `test_pending_moderation_manager_method` test method

#### Implementation Tasks - Manager
- [ ] [TICKET-021-17] Update `apps/forum/managers.py` to add ForumPostManager
- [ ] [TICKET-021-18] Create `ForumPostManager` class inheriting from models.Manager
- [ ] [TICKET-021-19] Implement `approved()` method filtering moderation_status='approved'
- [ ] [TICKET-021-20] Implement `visible()` method filtering approved and not deleted
- [ ] [TICKET-021-21] Implement `pending_moderation()` method filtering status='pending'
- [ ] [TICKET-021-22] Add docstrings to ForumPostManager and methods

#### Implementation Tasks - Model
- [ ] [TICKET-021-23] Update `apps/forum/models.py` to add ForumPost imports
- [ ] [TICKET-021-24] Create MODERATION_STATUS_CHOICES tuple
- [ ] [TICKET-021-25] Create `ForumPost` model class inheriting from models.Model
- [ ] [TICKET-021-26] Add `topic` field (ForeignKey to ForumTopic, on_delete=CASCADE, related_name='posts')
- [ ] [TICKET-021-27] Add `author` field (ForeignKey to User, on_delete=CASCADE, related_name='forum_posts')
- [ ] [TICKET-021-28] Add `content` field (TextField, max_length=10000)
- [ ] [TICKET-021-29] Add `is_first_post` field (BooleanField, default=False, db_index=True)
- [ ] [TICKET-021-30] Add `created_at` field (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-021-31] Add `updated_at` field (DateTimeField, auto_now=True)
- [ ] [TICKET-021-32] Add `edited_at` field (DateTimeField, null=True, blank=True)
- [ ] [TICKET-021-33] Add `edited_by` field (ForeignKey to User, null=True, on_delete=SET_NULL, related_name='+')
- [ ] [TICKET-021-34] Add `moderation_status` field (CharField with choices, default='approved', db_index=True)
- [ ] [TICKET-021-35] Add `moderation_details` field (JSONField, default=dict, blank=True)
- [ ] [TICKET-021-36] Add `is_deleted` field (BooleanField, default=False)
- [ ] [TICKET-021-37] Set objects = ForumPostManager()
- [ ] [TICKET-021-38] Implement `mark_as_edited(editor)` method
- [ ] [TICKET-021-39] Set edited_at to current time in mark_as_edited()
- [ ] [TICKET-021-40] Set edited_by to editor user in mark_as_edited()
- [ ] [TICKET-021-41] Save post
- [ ] [TICKET-021-42] Implement `soft_delete()` method
- [ ] [TICKET-021-43] Set is_deleted = True in soft_delete()
- [ ] [TICKET-021-44] Save post
- [ ] [TICKET-021-45] Implement `__str__()` method returning truncated content (50 chars)
- [ ] [TICKET-021-46] Add Meta class with db_table = 'forum_post'
- [ ] [TICKET-021-47] Add ordering = ['created_at'] to Meta
- [ ] [TICKET-021-48] Add composite index on (topic, created_at) to Meta
- [ ] [TICKET-021-49] Add index on (moderation_status, created_at) to Meta
- [ ] [TICKET-021-50] Add docstrings to ForumPost model and methods

#### Implementation Tasks - Signals
- [ ] [TICKET-021-51] Create `apps/forum/signals.py` with imports
- [ ] [TICKET-021-52] Import post_save signal and receiver decorator
- [ ] [TICKET-021-53] Import F expression for atomic updates
- [ ] [TICKET-021-54] Create `update_counts_on_post_save` function with @receiver decorator
- [ ] [TICKET-021-55] Connect to ForumPost post_save signal
- [ ] [TICKET-021-56] Check if instance is newly created
- [ ] [TICKET-021-57] Update ForumTopic.post_count using F() expression
- [ ] [TICKET-021-58] Call topic.update_last_post(instance)
- [ ] [TICKET-021-59] Update ForumCategory.post_count using F() expression
- [ ] [TICKET-021-60] Update UserProfile.forum_post_count using F() expression
- [ ] [TICKET-021-61] Add error handling and logging
- [ ] [TICKET-021-62] Add docstring to signal handler
- [ ] [TICKET-021-63] Update `apps/forum/apps.py` to import signals in ready() method

#### Admin Tasks
- [ ] [TICKET-021-64] Update `apps/forum/admin.py` to import ForumPost
- [ ] [TICKET-021-65] Create `ForumPostAdmin` class
- [ ] [TICKET-021-66] Add list_display (truncated content, author, topic, moderation_status, created_at)
- [ ] [TICKET-021-67] Add list_filter (moderation_status, is_deleted, is_first_post, created_at)
- [ ] [TICKET-021-68] Add search_fields (content, author__username, topic__title)
- [ ] [TICKET-021-69] Add readonly_fields (created_at, updated_at, edited_at, edited_by)
- [ ] [TICKET-021-70] Create `approve_posts` admin action
- [ ] [TICKET-021-71] Implement approve_posts to set moderation_status='approved'
- [ ] [TICKET-021-72] Create `reject_posts` admin action
- [ ] [TICKET-021-73] Implement reject_posts to set moderation_status='rejected'
- [ ] [TICKET-021-74] Add actions to ForumPostAdmin
- [ ] [TICKET-021-75] Register ForumPost with ForumPostAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-021-76] Run `python manage.py makemigrations forum`
- [ ] [TICKET-021-77] Run `python manage.py migrate`
- [ ] [TICKET-021-78] Run `python manage.py check`
- [ ] [TICKET-021-79] Run `pytest apps/forum/tests/test_posts.py -v`
- [ ] [TICKET-021-80] Verify all tests pass
- [ ] [TICKET-021-81] Create test ForumPost in admin
- [ ] [TICKET-021-82] Verify topic post_count incremented
- [ ] [TICKET-021-83] Verify category post_count incremented
- [ ] [TICKET-021-84] Verify user profile forum_post_count incremented
- [ ] [TICKET-021-85] Verify topic last_post_at and last_post_by updated
- [ ] [TICKET-021-86] Test mark_as_edited() method
- [ ] [TICKET-021-87] Test soft_delete() method
- [ ] [TICKET-021-88] Test manager methods (approved, visible, pending_moderation)

---

### TICKET-022: Forum Views - Category and Topic Listing
**Dependencies:** TICKET-021

#### Test Tasks
- [ ] [TICKET-022-01] Create `apps/forum/tests/test_views.py` with imports
- [ ] [TICKET-022-02] Add `TestForumIndexView` test class
- [ ] [TICKET-022-03] Write `test_forum_index_displays_categories` test method
- [ ] [TICKET-022-04] Write `test_forum_index_shows_stats` test method
- [ ] [TICKET-022-05] Add `TestCategoryDetailView` test class
- [ ] [TICKET-022-06] Write `test_category_detail_displays_topics` test method
- [ ] [TICKET-022-07] Write `test_category_detail_pagination` test method
- [ ] [TICKET-022-08] Write `test_category_detail_pinned_topics_first` test method
- [ ] [TICKET-022-09] Add `TestTopicDetailView` test class
- [ ] [TICKET-022-10] Write `test_topic_detail_displays_posts` test method
- [ ] [TICKET-022-11] Write `test_topic_detail_pagination` test method
- [ ] [TICKET-022-12] Write `test_topic_detail_increments_view_count` test method
- [ ] [TICKET-022-13] Write `test_topic_detail_shows_reply_form_when_authenticated` test method

#### Implementation Tasks - Template Tags
- [ ] [TICKET-022-14] Create `apps/forum/templatetags/` directory
- [ ] [TICKET-022-15] Create `apps/forum/templatetags/__init__.py`
- [ ] [TICKET-022-16] Create `apps/forum/templatetags/forum_tags.py` with imports
- [ ] [TICKET-022-17] Register template library
- [ ] [TICKET-022-18] Create `user_can_edit_post` filter
- [ ] [TICKET-022-19] Implement user_can_edit_post to check ownership or moderator status
- [ ] [TICKET-022-20] Create `user_can_delete_post` filter
- [ ] [TICKET-022-21] Implement user_can_delete_post to check ownership or moderator status
- [ ] [TICKET-022-22] Create `format_post_content` filter
- [ ] [TICKET-022-23] Implement format_post_content to render markdown
- [ ] [TICKET-022-24] Add line break conversion in format_post_content
- [ ] [TICKET-022-25] Add docstrings to all template tags

#### Implementation Tasks - Views
- [ ] [TICKET-022-26] Create `apps/forum/views.py` with imports
- [ ] [TICKET-022-27] Create `ForumIndexView` class inheriting from TemplateView
- [ ] [TICKET-022-28] Set template_name = 'forum/index.html'
- [ ] [TICKET-022-29] Override get_context_data() to fetch active categories
- [ ] [TICKET-022-30] Add category stats to context
- [ ] [TICKET-022-31] Add recent topics to context (last 10)
- [ ] [TICKET-022-32] Create `CategoryDetailView` class inheriting from ListView
- [ ] [TICKET-022-33] Set model = ForumTopic
- [ ] [TICKET-022-34] Set template_name = 'forum/category_detail.html'
- [ ] [TICKET-022-35] Set context_object_name = 'topics'
- [ ] [TICKET-022-36] Set paginate_by = 25
- [ ] [TICKET-022-37] Override get_queryset() to filter by category slug
- [ ] [TICKET-022-38] Order queryset by is_pinned and last_post_at
- [ ] [TICKET-022-39] Add sorting options (recent, popular) from query params
- [ ] [TICKET-022-40] Override get_context_data() to add category object
- [ ] [TICKET-022-41] Create `TopicDetailView` class inheriting from ListView
- [ ] [TICKET-022-42] Set model = ForumPost
- [ ] [TICKET-022-43] Set template_name = 'forum/topic_detail.html'
- [ ] [TICKET-022-44] Set context_object_name = 'posts'
- [ ] [TICKET-022-45] Set paginate_by = 20
- [ ] [TICKET-022-46] Override get_queryset() to filter by topic slug
- [ ] [TICKET-022-47] Filter visible posts only
- [ ] [TICKET-022-48] Order by created_at
- [ ] [TICKET-022-49] Override get() to increment topic view_count
- [ ] [TICKET-022-50] Override get_context_data() to add topic object
- [ ] [TICKET-022-51] Add reply form to context if user authenticated
- [ ] [TICKET-022-52] Add docstrings to all views

#### Implementation Tasks - Templates
- [ ] [TICKET-022-53] Create `apps/forum/templates/` directory
- [ ] [TICKET-022-54] Create `apps/forum/templates/forum/` directory
- [ ] [TICKET-022-55] Create `apps/forum/templates/forum/index.html` extending base.html
- [ ] [TICKET-022-56] Add page title "Community Forum"
- [ ] [TICKET-022-57] Create categories list section
- [ ] [TICKET-022-58] Loop through categories and display name, description
- [ ] [TICKET-022-59] Display topic_count and post_count for each category
- [ ] [TICKET-022-60] Add link to category detail page
- [ ] [TICKET-022-61] Create recent activity section
- [ ] [TICKET-022-62] Display last 10 topics with links
- [ ] [TICKET-022-63] Create `apps/forum/templates/forum/category_detail.html` extending base.html
- [ ] [TICKET-022-64] Add category name as page title
- [ ] [TICKET-022-65] Display category description
- [ ] [TICKET-022-66] Add "New Topic" button (if authenticated)
- [ ] [TICKET-022-67] Add filter/sort dropdown (recent, popular)
- [ ] [TICKET-022-68] Create topics table with columns (title, author, replies, views, last post)
- [ ] [TICKET-022-69] Loop through topics and display data
- [ ] [TICKET-022-70] Add pinned badge for pinned topics
- [ ] [TICKET-022-71] Add locked icon for locked topics
- [ ] [TICKET-022-72] Add pagination controls
- [ ] [TICKET-022-73] Create `apps/forum/templates/forum/topic_detail.html` extending base.html
- [ ] [TICKET-022-74] Add topic title as page title
- [ ] [TICKET-022-75] Display topic metadata (author, created date, views)
- [ ] [TICKET-022-76] Create posts list section
- [ ] [TICKET-022-77] Loop through posts and display each post
- [ ] [TICKET-022-78] Create post card with author sidebar
- [ ] [TICKET-022-79] Display author avatar, username, post count in sidebar
- [ ] [TICKET-022-80] Display post content using format_post_content filter
- [ ] [TICKET-022-81] Display post created_at and edited_at if applicable
- [ ] [TICKET-022-82] Add edit/delete buttons if user_can_edit_post
- [ ] [TICKET-022-83] Add pagination controls for posts
- [ ] [TICKET-022-84] Add reply form at bottom (if authenticated and not locked)
- [ ] [TICKET-022-85] Add HTMX attributes for inline reply

#### Implementation Tasks - URLs
- [ ] [TICKET-022-86] Create `apps/forum/urls.py` with imports
- [ ] [TICKET-022-87] Set app_name = 'forum'
- [ ] [TICKET-022-88] Add URL pattern for ForumIndexView (path '', name='index')
- [ ] [TICKET-022-89] Add URL pattern for CategoryDetailView (path '<slug:category_slug>/', name='category_detail')
- [ ] [TICKET-022-90] Add URL pattern for TopicDetailView (path '<slug:category_slug>/<slug:topic_slug>/', name='topic_detail')
- [ ] [TICKET-022-91] Update `config/urls.py` to include forum.urls at 'forum/'

#### Navigation Tasks
- [ ] [TICKET-022-92] Update `templates/components/navbar.html` to add Forum link
- [ ] [TICKET-022-93] Add link to forum:index

#### Verification Tasks
- [ ] [TICKET-022-94] Create test categories and topics in database
- [ ] [TICKET-022-95] Start development server
- [ ] [TICKET-022-96] Access forum index and verify categories display
- [ ] [TICKET-022-97] Click on category and verify topics display
- [ ] [TICKET-022-98] Verify pagination works on category page
- [ ] [TICKET-022-99] Verify pinned topics appear first
- [ ] [TICKET-022-100] Click on topic and verify posts display
- [ ] [TICKET-022-101] Verify pagination works on topic page
- [ ] [TICKET-022-102] Verify view count increments on topic view
- [ ] [TICKET-022-103] Verify reply form shows when authenticated
- [ ] [TICKET-022-104] Verify edit/delete buttons show for own posts
- [ ] [TICKET-022-105] Run `pytest apps/forum/tests/test_views.py -v`
- [ ] [TICKET-022-106] Verify all tests pass

---

### TICKET-023: Forum Views - Topic and Post Creation
**Dependencies:** TICKET-022

#### Test Tasks
- [ ] [TICKET-023-01] Create `apps/forum/tests/test_topic_creation.py` with imports
- [ ] [TICKET-023-02] Add `TestTopicCreateView` test class
- [ ] [TICKET-023-03] Write `test_topic_create_view_requires_authentication` test method
- [ ] [TICKET-023-04] Write `test_topic_create_view_get` test method
- [ ] [TICKET-023-05] Write `test_topic_create_view_post_valid` test method
- [ ] [TICKET-023-06] Write `test_topic_create_creates_first_post` test method
- [ ] [TICKET-023-07] Create `apps/forum/tests/test_post_creation.py` with imports
- [ ] [TICKET-023-08] Add `TestPostCreateView` test class
- [ ] [TICKET-023-09] Write `test_post_create_view_requires_authentication` test method
- [ ] [TICKET-023-10] Write `test_post_create_view_post_valid` test method
- [ ] [TICKET-023-11] Write `test_post_create_updates_topic` test method
- [ ] [TICKET-023-12] Write `test_post_create_rate_limiting` test method
- [ ] [TICKET-023-13] Add `TestPostEditView` test class
- [ ] [TICKET-023-14] Write `test_post_edit_view_requires_ownership` test method
- [ ] [TICKET-023-15] Write `test_post_edit_view_post_valid` test method
- [ ] [TICKET-023-16] Write `test_post_edit_marks_as_edited` test method
- [ ] [TICKET-023-17] Add `TestPostDeleteView` test class
- [ ] [TICKET-023-18] Write `test_post_delete_view_requires_ownership` test method
- [ ] [TICKET-023-19] Write `test_post_delete_soft_deletes` test method

#### Implementation Tasks - Permissions
- [ ] [TICKET-023-20] Create `apps/forum/permissions.py` with imports
- [ ] [TICKET-023-21] Create `can_create_topic(user, category)` function
- [ ] [TICKET-023-22] Check if user is authenticated in can_create_topic()
- [ ] [TICKET-023-23] Check if category is active
- [ ] [TICKET-023-24] Return boolean
- [ ] [TICKET-023-25] Create `can_reply_to_topic(user, topic)` function
- [ ] [TICKET-023-26] Check if user is authenticated
- [ ] [TICKET-023-27] Check if topic is not locked
- [ ] [TICKET-023-28] Return boolean
- [ ] [TICKET-023-29] Create `can_edit_post(user, post)` function
- [ ] [TICKET-023-30] Check if user is post author or has moderator permissions
- [ ] [TICKET-023-31] Return boolean
- [ ] [TICKET-023-32] Create `can_delete_post(user, post)` function
- [ ] [TICKET-023-33] Check if user is post author or has moderator permissions
- [ ] [TICKET-023-34] Return boolean
- [ ] [TICKET-023-35] Add docstrings to all permission functions

#### Implementation Tasks - Forms
- [ ] [TICKET-023-36] Create `apps/forum/forms.py` with imports
- [ ] [TICKET-023-37] Create `TopicCreateForm` class inheriting from forms.Form
- [ ] [TICKET-023-38] Add `title` field (CharField, max_length=255)
- [ ] [TICKET-023-39] Add `content` field (CharField, widget=Textarea, max_length=10000)
- [ ] [TICKET-023-40] Implement `clean_title()` to check length and spam patterns
- [ ] [TICKET-023-41] Implement `clean_content()` to check length
- [ ] [TICKET-023-42] Add docstring to TopicCreateForm
- [ ] [TICKET-023-43] Create `PostCreateForm` class inheriting from forms.Form
- [ ] [TICKET-023-44] Add `content` field (CharField, widget=Textarea, max_length=10000)
- [ ] [TICKET-023-45] Implement `clean_content()` to check length
- [ ] [TICKET-023-46] Add docstring to PostCreateForm
- [ ] [TICKET-023-47] Create `PostEditForm` class inheriting from forms.ModelForm
- [ ] [TICKET-023-48] Add Meta class with ForumPost model
- [ ] [TICKET-023-49] Set fields = ['content']
- [ ] [TICKET-023-50] Add widget for content (Textarea)
- [ ] [TICKET-023-51] Add docstring to PostEditForm

#### Implementation Tasks - Rate Limiting
- [ ] [TICKET-023-52] Create `apps/forum/utils.py` with imports
- [ ] [TICKET-023-53] Import Django cache
- [ ] [TICKET-023-54] Create `check_rate_limit(user, action='post')` function
- [ ] [TICKET-023-55] Build cache key from user ID and action
- [ ] [TICKET-023-56] Get current count from cache
- [ ] [TICKET-023-57] Check if count exceeds limit (5 posts per 5 minutes)
- [ ] [TICKET-023-58] Return boolean (True if allowed, False if rate limited)
- [ ] [TICKET-023-59] Create `increment_rate_limit(user, action='post')` function
- [ ] [TICKET-023-60] Build cache key
- [ ] [TICKET-023-61] Increment count in cache with 5 minute TTL
- [ ] [TICKET-023-62] Add docstrings to rate limiting functions

#### Implementation Tasks - Views
- [ ] [TICKET-023-63] Update `apps/forum/views.py` to add creation views
- [ ] [TICKET-023-64] Import LoginRequiredMixin, permission functions, forms
- [ ] [TICKET-023-65] Create `TopicCreateView` class inheriting from LoginRequiredMixin, CreateView
- [ ] [TICKET-023-66] Set template_name = 'forum/topic_create.html'
- [ ] [TICKET-023-67] Set form_class = TopicCreateForm
- [ ] [TICKET-023-68] Override dispatch() to check can_create_topic permission
- [ ] [TICKET-023-69] Override form_valid() to create topic and first post
- [ ] [TICKET-023-70] Set topic.creator to request.user
- [ ] [TICKET-023-71] Generate slug from title
- [ ] [TICKET-023-72] Save topic
- [ ] [TICKET-023-73] Create first ForumPost with is_first_post=True
- [ ] [TICKET-023-74] Set success_url to topic detail page
- [ ] [TICKET-023-75] Add success message
- [ ] [TICKET-023-76] Create `PostCreateView` class inheriting from LoginRequiredMixin, CreateView
- [ ] [TICKET-023-77] Set form_class = PostCreateForm
- [ ] [TICKET-023-78] Override dispatch() to check can_reply_to_topic permission
- [ ] [TICKET-023-79] Override dispatch() to check rate limit
- [ ] [TICKET-023-80] Show error message if rate limited
- [ ] [TICKET-023-81] Override form_valid() to create post
- [ ] [TICKET-023-82] Set post.topic from URL parameter
- [ ] [TICKET-023-83] Set post.author to request.user
- [ ] [TICKET-023-84] Save post
- [ ] [TICKET-023-85] Increment rate limit counter
- [ ] [TICKET-023-86] Set success_url to topic detail page (last page)
- [ ] [TICKET-023-87] Add success message
- [ ] [TICKET-023-88] Create `PostEditView` class inheriting from LoginRequiredMixin, UpdateView
- [ ] [TICKET-023-89] Set model = ForumPost
- [ ] [TICKET-023-90] Set template_name = 'forum/post_edit.html'
- [ ] [TICKET-023-91] Set form_class = PostEditForm
- [ ] [TICKET-023-92] Override dispatch() to check can_edit_post permission
- [ ] [TICKET-023-93] Override form_valid() to call post.mark_as_edited(request.user)
- [ ] [TICKET-023-94] Set success_url to topic detail page
- [ ] [TICKET-023-95] Add success message
- [ ] [TICKET-023-96] Create `PostDeleteView` class inheriting from LoginRequiredMixin, View
- [ ] [TICKET-023-97] Override dispatch() to check can_delete_post permission
- [ ] [TICKET-023-98] Implement post() method to call post.soft_delete()
- [ ] [TICKET-023-99] Redirect to topic detail page
- [ ] [TICKET-023-100] Add success message
- [ ] [TICKET-023-101] Add docstrings to all views

#### Implementation Tasks - Templates
- [ ] [TICKET-023-102] Create `apps/forum/templates/forum/topic_create.html` extending base.html
- [ ] [TICKET-023-103] Add page title "Create New Topic"
- [ ] [TICKET-023-104] Display category name
- [ ] [TICKET-023-105] Add topic creation form with title and content fields
- [ ] [TICKET-023-106] Add CSRF token and submit button
- [ ] [TICKET-023-107] Add cancel button linking back to category
- [ ] [TICKET-023-108] Create `apps/forum/templates/forum/post_edit.html` extending base.html
- [ ] [TICKET-023-109] Add page title "Edit Post"
- [ ] [TICKET-023-110] Add post edit form with content field
- [ ] [TICKET-023-111] Add CSRF token and submit button
- [ ] [TICKET-023-112] Add cancel button linking back to topic
- [ ] [TICKET-023-113] Update `apps/forum/templates/forum/category_detail.html`
- [ ] [TICKET-023-114] Add "New Topic" button at top (if authenticated)
- [ ] [TICKET-023-115] Link button to topic_create view
- [ ] [TICKET-023-116] Update `apps/forum/templates/forum/topic_detail.html`
- [ ] [TICKET-023-117] Add reply form at bottom (if authenticated and not locked)
- [ ] [TICKET-023-118] Use PostCreateForm
- [ ] [TICKET-023-119] Add HTMX attributes for inline submission
- [ ] [TICKET-023-120] Add edit button to each post (if user_can_edit_post)
- [ ] [TICKET-023-121] Add delete button to each post (if user_can_delete_post)

#### Implementation Tasks - URLs
- [ ] [TICKET-023-122] Update `apps/forum/urls.py` to add creation URLs
- [ ] [TICKET-023-123] Add URL pattern for TopicCreateView (path '<slug:category_slug>/new/', name='topic_create')
- [ ] [TICKET-023-124] Add URL pattern for PostCreateView (path '<slug:category_slug>/<slug:topic_slug>/reply/', name='post_create')
- [ ] [TICKET-023-125] Add URL pattern for PostEditView (path 'post/<int:pk>/edit/', name='post_edit')
- [ ] [TICKET-023-126] Add URL pattern for PostDeleteView (path 'post/<int:pk>/delete/', name='post_delete')

#### Verification Tasks
- [ ] [TICKET-023-127] Login as test user
- [ ] [TICKET-023-128] Access category page and click "New Topic"
- [ ] [TICKET-023-129] Fill out topic form and submit
- [ ] [TICKET-023-130] Verify topic created with first post
- [ ] [TICKET-023-131] Verify redirected to new topic page
- [ ] [TICKET-023-132] Submit reply using reply form
- [ ] [TICKET-023-133] Verify post created and appears in topic
- [ ] [TICKET-023-134] Verify topic last_post_at updated
- [ ] [TICKET-023-135] Click edit button on own post
- [ ] [TICKET-023-136] Edit content and submit
- [ ] [TICKET-023-137] Verify post updated and marked as edited
- [ ] [TICKET-023-138] Test rate limiting by creating 6 posts quickly
- [ ] [TICKET-023-139] Verify error message on 6th post
- [ ] [TICKET-023-140] Test delete button on own post
- [ ] [TICKET-023-141] Verify post soft deleted
- [ ] [TICKET-023-142] Try to reply to locked topic (create locked topic first)
- [ ] [TICKET-023-143] Verify error message shown
- [ ] [TICKET-023-144] Run `pytest apps/forum/tests/test_topic_creation.py -v`
- [ ] [TICKET-023-145] Run `pytest apps/forum/tests/test_post_creation.py -v`
- [ ] [TICKET-023-146] Verify all tests pass

---

## PHASE 4: AI AVATARS & MODERATION

### TICKET-024: AI Avatar Model and Management
**Dependencies:** TICKET-019, TICKET-014

#### Test Tasks
- [ ] [TICKET-024-01] Create `apps/users/tests/test_ai_avatar.py` with imports
- [ ] [TICKET-024-02] Add `TestAIAvatarModel` test class
- [ ] [TICKET-024-03] Write `test_ai_avatar_creation` test method
- [ ] [TICKET-024-04] Write `test_slug_auto_generation` test method
- [ ] [TICKET-024-05] Write `test_can_participate_in_topic` test method
- [ ] [TICKET-024-06] Write `test_get_participation_prompt` test method
- [ ] [TICKET-024-07] Write `test_str_method` test method
- [ ] [TICKET-024-08] Add `TestAIAvatarService` test class
- [ ] [TICKET-024-09] Write `test_get_avatar_for_topic` test method
- [ ] [TICKET-024-10] Write `test_should_avatar_participate` test method
- [ ] [TICKET-024-11] Write `test_generate_avatar_response` test method (mocked AI)

#### Implementation Tasks - Model
- [ ] [TICKET-024-12] Update `apps/users/models.py` to add AIAvatar imports
- [ ] [TICKET-024-13] Create `AIAvatar` model class inheriting from TimeStampedModel
- [ ] [TICKET-024-14] Add `name` field (CharField, max_length=100, unique=True)
- [ ] [TICKET-024-15] Add `slug` field (SlugField, unique=True, db_index=True, max_length=110)
- [ ] [TICKET-024-16] Add `persona_description` field (TextField)
- [ ] [TICKET-024-17] Add `short_bio` field (CharField, max_length=200)
- [ ] [TICKET-024-18] Add `avatar` field (ImageField, upload_to='ai_avatars/', null=True, blank=True)
- [ ] [TICKET-024-19] Add `generation_rules` field (JSONField, default=dict, blank=True)
- [ ] [TICKET-024-20] Add `expertise_areas` field (ArrayField of CharField, default=list, blank=True)
- [ ] [TICKET-024-21] Add `is_active` field (BooleanField, default=True, db_index=True)
- [ ] [TICKET-024-22] Add `post_count` field (IntegerField, default=0)
- [ ] [TICKET-024-23] Add `last_active_at` field (DateTimeField, null=True, blank=True)
- [ ] [TICKET-024-24] Override `save()` method to auto-generate slug from name
- [ ] [TICKET-024-25] Implement `can_participate_in_topic(topic)` method
- [ ] [TICKET-024-26] Check if topic keywords match expertise_areas
- [ ] [TICKET-024-27] Return boolean
- [ ] [TICKET-024-28] Implement `get_participation_prompt(context)` method
- [ ] [TICKET-024-29] Build prompt with persona_description and context
- [ ] [TICKET-024-30] Apply generation_rules to prompt
- [ ] [TICKET-024-31] Return formatted prompt string
- [ ] [TICKET-024-32] Implement `__str__()` method returning name
- [ ] [TICKET-024-33] Add Meta class with db_table = 'users_ai_avatar'
- [ ] [TICKET-024-34] Add ordering = ['name'] to Meta
- [ ] [TICKET-024-35] Add docstrings to AIAvatar model and methods

#### Implementation Tasks - Update ForumPost
- [ ] [TICKET-024-36] Update `apps/forum/models.py` ForumPost model
- [ ] [TICKET-024-37] Change `author` field to allow null=True, blank=True
- [ ] [TICKET-024-38] Add `author_avatar` field (ForeignKey to AIAvatar, null=True, blank=True, on_delete=SET_NULL, related_name='forum_posts')
- [ ] [TICKET-024-39] Add clean() method to validate either author or author_avatar is set
- [ ] [TICKET-024-40] Update `__str__()` to handle both human and AI authors
- [ ] [TICKET-024-41] Add docstring explaining author constraint

#### Implementation Tasks - Services
- [ ] [TICKET-024-42] Create `apps/users/services.py` with imports
- [ ] [TICKET-024-43] Import AIAvatar, AIService
- [ ] [TICKET-024-44] Create `AIAvatarService` class
- [ ] [TICKET-024-45] Implement `get_avatar_for_topic(topic)` method
- [ ] [TICKET-024-46] Extract keywords from topic title
- [ ] [TICKET-024-47] Query active AIAvatars
- [ ] [TICKET-024-48] Filter by matching expertise_areas
- [ ] [TICKET-024-49] Return best matching avatar or None
- [ ] [TICKET-024-50] Implement `should_avatar_participate(avatar, topic)` method
- [ ] [TICKET-024-51] Check avatar.can_participate_in_topic(topic)
- [ ] [TICKET-024-52] Check avatar activity frequency (not too frequent)
- [ ] [TICKET-024-53] Return boolean decision
- [ ] [TICKET-024-54] Implement `generate_avatar_response(avatar, context, question=None)` method
- [ ] [TICKET-024-55] Build prompt using avatar.get_participation_prompt(context)
- [ ] [TICKET-024-56] Add question to prompt if provided
- [ ] [TICKET-024-57] Call AIService.generate_text() with prompt
- [ ] [TICKET-024-58] Return generated response
- [ ] [TICKET-024-59] Add error handling and logging
- [ ] [TICKET-024-60] Add docstrings to AIAvatarService and methods

#### Implementation Tasks - Management Command
- [ ] [TICKET-024-61] Create `apps/users/management/` directory
- [ ] [TICKET-024-62] Create `apps/users/management/__init__.py`
- [ ] [TICKET-024-63] Create `apps/users/management/commands/` directory
- [ ] [TICKET-024-64] Create `apps/users/management/commands/__init__.py`
- [ ] [TICKET-024-65] Create `apps/users/management/commands/create_default_avatars.py`
- [ ] [TICKET-024-66] Create Command class
- [ ] [TICKET-024-67] Implement handle() method
- [ ] [TICKET-024-68] Create "Frugal Fred" avatar with budgeting expertise
- [ ] [TICKET-024-69] Create "Savvy Sarah" avatar with saving strategies expertise
- [ ] [TICKET-024-70] Create "Investment Ian" avatar with investment expertise
- [ ] [TICKET-024-71] Create "Deal Hunter Diana" avatar with deals expertise
- [ ] [TICKET-024-72] Create "Minimalist Mike" avatar with minimalism expertise
- [ ] [TICKET-024-73] Set persona_description for each avatar
- [ ] [TICKET-024-74] Set expertise_areas for each avatar
- [ ] [TICKET-024-75] Set generation_rules for each avatar
- [ ] [TICKET-024-76] Add output messages showing created avatars

#### Admin Tasks
- [ ] [TICKET-024-77] Update `apps/users/admin.py` to import AIAvatar
- [ ] [TICKET-024-78] Create `AIAvatarAdmin` class
- [ ] [TICKET-024-79] Add list_display (name, is_active, post_count, last_active_at)
- [ ] [TICKET-024-80] Add list_filter (is_active, expertise_areas, created_at)
- [ ] [TICKET-024-81] Add search_fields (name, persona_description, short_bio)
- [ ] [TICKET-024-82] Add readonly_fields (slug, post_count, last_active_at, created_at)
- [ ] [TICKET-024-83] Add fieldsets for better organization (Basic Info, Persona, Activity)
- [ ] [TICKET-024-84] Create `activate_avatars` admin action
- [ ] [TICKET-024-85] Create `deactivate_avatars` admin action
- [ ] [TICKET-024-86] Add actions to AIAvatarAdmin
- [ ] [TICKET-024-87] Register AIAvatar with AIAvatarAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-024-88] Run `python manage.py makemigrations users`
- [ ] [TICKET-024-89] Run `python manage.py makemigrations forum` (for ForumPost changes)
- [ ] [TICKET-024-90] Run `python manage.py migrate`
- [ ] [TICKET-024-91] Run `python manage.py check`
- [ ] [TICKET-024-92] Run `python manage.py create_default_avatars`
- [ ] [TICKET-024-93] Verify 5 avatars created in database
- [ ] [TICKET-024-94] Check admin and verify avatars display correctly
- [ ] [TICKET-024-95] Test can_participate_in_topic() with test topic
- [ ] [TICKET-024-96] Test get_avatar_for_topic() with test topic
- [ ] [TICKET-024-97] Test generate_avatar_response() with mocked AI
- [ ] [TICKET-024-98] Run `pytest apps/users/tests/test_ai_avatar.py -v`
- [ ] [TICKET-024-99] Verify all tests pass

---

### TICKET-025: AI Avatar Forum Participation - Topic Initiation
**Dependencies:** TICKET-024, TICKET-015

#### Test Tasks
- [ ] [TICKET-025-01] Create `apps/forum/tests/test_ai_participation.py` with imports
- [ ] [TICKET-025-02] Add `TestAITopicInitiation` test class
- [ ] [TICKET-025-03] Write `test_ai_avatar_initiate_topic_from_article` test method (mocked)
- [ ] [TICKET-025-04] Write `test_schedule_ai_topic_initiation` test method (mocked)
- [ ] [TICKET-025-05] Write `test_create_topic_from_article` test method
- [ ] [TICKET-025-06] Write `test_generate_discussion_starter` test method (mocked AI)

#### Implementation Tasks - Prompts
- [ ] [TICKET-025-07] Create `apps/forum/prompts.py` with imports
- [ ] [TICKET-025-08] Create `TOPIC_INITIATION_PROMPT` template string
- [ ] [TICKET-025-09] Add article summary placeholder to prompt
- [ ] [TICKET-025-10] Add key points placeholder to prompt
- [ ] [TICKET-025-11] Add engaging question instructions
- [ ] [TICKET-025-12] Add persona maintenance instructions
- [ ] [TICKET-025-13] Add docstring explaining prompt usage

#### Implementation Tasks - Services
- [ ] [TICKET-025-14] Create `apps/forum/services.py` with imports
- [ ] [TICKET-025-15] Import AIService, AIAvatarService, prompts
- [ ] [TICKET-025-16] Create `ForumAIService` class
- [ ] [TICKET-025-17] Implement `create_topic_from_article(article, avatar)` method
- [ ] [TICKET-025-18] Generate discussion starter using generate_discussion_starter()
- [ ] [TICKET-025-19] Create ForumTopic with appropriate category
- [ ] [TICKET-025-20] Set topic.creator to None (AI topic)
- [ ] [TICKET-025-21] Create first ForumPost with author_avatar=avatar
- [ ] [TICKET-025-22] Set is_first_post=True
- [ ] [TICKET-025-23] Save topic and post
- [ ] [TICKET-025-24] Return topic instance
- [ ] [TICKET-025-25] Implement `generate_discussion_starter(article, avatar)` method
- [ ] [TICKET-025-26] Build context with article summary and key points
- [ ] [TICKET-025-27] Format TOPIC_INITIATION_PROMPT with context
- [ ] [TICKET-025-28] Call AIService.generate_text() with prompt
- [ ] [TICKET-025-29] Return generated discussion starter
- [ ] [TICKET-025-30] Add error handling and logging
- [ ] [TICKET-025-31] Add docstrings to ForumAIService and methods

#### Implementation Tasks - Tasks
- [ ] [TICKET-025-32] Create `apps/forum/tasks.py` with imports
- [ ] [TICKET-025-33] Create `ai_avatar_initiate_topic_from_article(article_id, avatar_id=None)` function with @shared_task
- [ ] [TICKET-025-34] Fetch GeneratedArticle by ID
- [ ] [TICKET-025-35] Select appropriate AIAvatar if not provided
- [ ] [TICKET-025-36] Instantiate ForumAIService
- [ ] [TICKET-025-37] Call create_topic_from_article(article, avatar)
- [ ] [TICKET-025-38] Update avatar.last_active_at
- [ ] [TICKET-025-39] Increment avatar.post_count
- [ ] [TICKET-025-40] Log success with topic ID
- [ ] [TICKET-025-41] Handle exceptions and log errors
- [ ] [TICKET-025-42] Return topic ID or error status
- [ ] [TICKET-025-43] Create `schedule_ai_topic_initiation()` function with @shared_task
- [ ] [TICKET-025-44] Find recent GeneratedArticles without forum topics
- [ ] [TICKET-025-45] Select top 1-2 articles by view_count or date
- [ ] [TICKET-025-46] Loop through selected articles
- [ ] [TICKET-025-47] Dispatch ai_avatar_initiate_topic_from_article task for each
- [ ] [TICKET-025-48] Log scheduled tasks
- [ ] [TICKET-025-49] Return count of scheduled tasks
- [ ] [TICKET-025-50] Add docstrings to tasks

#### Implementation Tasks - Beat Schedule
- [ ] [TICKET-025-51] Update CELERY_BEAT_SCHEDULE in `config/settings/base.py`
- [ ] [TICKET-025-52] Add 'ai-initiate-topics' task entry
- [ ] [TICKET-025-53] Set schedule to crontab(hour=10, minute=0) for 10 AM daily

#### Settings Tasks
- [ ] [TICKET-025-54] Add AI_FORUM_PARTICIPATION_ENABLED = True to `config/settings/base.py`
- [ ] [TICKET-025-55] Add AI_TOPIC_INITIATION_ENABLED = True
- [ ] [TICKET-025-56] Add AI_MAX_TOPICS_PER_DAY = 2

#### Template Tasks
- [ ] [TICKET-025-57] Update `apps/forum/templates/forum/category_detail.html`
- [ ] [TICKET-025-58] Add "AI Discussion" badge for AI-initiated topics
- [ ] [TICKET-025-59] Update `apps/forum/templates/forum/topic_detail.html`
- [ ] [TICKET-025-60] Display AI avatar icon and name for AI posts
- [ ] [TICKET-025-61] Add disclaimer about AI participation

#### Verification Tasks
- [ ] [TICKET-025-62] Create test GeneratedArticle
- [ ] [TICKET-025-63] Run ai_avatar_initiate_topic_from_article task manually
- [ ] [TICKET-025-64] Verify ForumTopic created
- [ ] [TICKET-025-65] Verify first post created with AI author
- [ ] [TICKET-025-66] Verify AI avatar displayed correctly in forum
- [ ] [TICKET-025-67] Run schedule_ai_topic_initiation task
- [ ] [TICKET-025-68] Verify tasks dispatched for articles
- [ ] [TICKET-025-69] Run `pytest apps/forum/tests/test_ai_participation.py -v`
- [ ] [TICKET-025-70] Verify all tests pass

---

### TICKET-026: AI Avatar Forum Participation - Q&A Responses
**Dependencies:** TICKET-025

#### Test Tasks
- [ ] [TICKET-026-01] Add `TestAIMentionResponses` test class to test_ai_participation.py
- [ ] [TICKET-026-02] Write `test_ai_avatar_respond_to_mention` test method (mocked)
- [ ] [TICKET-026-03] Write `test_detect_avatar_mentions` test method
- [ ] [TICKET-026-04] Write `test_extract_mentions` test method
- [ ] [TICKET-026-05] Write `test_get_mentioned_avatars` test method
- [ ] [TICKET-026-06] Write `test_get_conversation_context` test method

#### Implementation Tasks - Utils
- [ ] [TICKET-026-07] Create `apps/forum/utils.py` with imports
- [ ] [TICKET-026-08] Import re for regex
- [ ] [TICKET-026-09] Create `extract_mentions(text)` function
- [ ] [TICKET-026-10] Use regex to find @mentions in text
- [ ] [TICKET-026-11] Return list of mentioned names
- [ ] [TICKET-026-12] Create `get_mentioned_avatars(post)` function
- [ ] [TICKET-026-13] Extract mentions from post.content
- [ ] [TICKET-026-14] Query AIAvatar by name (case-insensitive)
- [ ] [TICKET-026-15] Return queryset of mentioned avatars
- [ ] [TICKET-026-16] Create `get_conversation_context(post, num_posts=5)` function
- [ ] [TICKET-026-17] Get recent posts in same topic
- [ ] [TICKET-026-18] Limit to num_posts
- [ ] [TICKET-026-19] Return list of posts with author and content
- [ ] [TICKET-026-20] Add docstrings to util functions

#### Implementation Tasks - Prompts
- [ ] [TICKET-026-21] Update `apps/forum/prompts.py` to add QA_RESPONSE_PROMPT
- [ ] [TICKET-026-22] Create `QA_RESPONSE_PROMPT` template string
- [ ] [TICKET-026-23] Add conversation context placeholder
- [ ] [TICKET-026-24] Add question/mention placeholder
- [ ] [TICKET-026-25] Add relevant knowledge placeholder
- [ ] [TICKET-026-26] Add persona maintenance instructions
- [ ] [TICKET-026-27] Add concise response instructions
- [ ] [TICKET-026-28] Add docstring explaining prompt usage

#### Implementation Tasks - Services
- [ ] [TICKET-026-29] Update `apps/forum/services.py` ForumAIService class
- [ ] [TICKET-026-30] Implement `generate_response_to_mention(post, avatar)` method
- [ ] [TICKET-026-31] Get conversation context using get_conversation_context()
- [ ] [TICKET-026-32] Search for relevant ProcessedContent based on topic keywords
- [ ] [TICKET-026-33] Build context dictionary with conversation and knowledge
- [ ] [TICKET-026-34] Format QA_RESPONSE_PROMPT with context
- [ ] [TICKET-026-35] Call AIService.generate_text() with prompt
- [ ] [TICKET-026-36] Return generated response text
- [ ] [TICKET-026-37] Add error handling and logging
- [ ] [TICKET-026-38] Add docstring to method

#### Implementation Tasks - Tasks
- [ ] [TICKET-026-39] Update `apps/forum/tasks.py` to add mention response tasks
- [ ] [TICKET-026-40] Create `ai_avatar_respond_to_mention(post_id, avatar_id)` function with @shared_task
- [ ] [TICKET-026-41] Fetch ForumPost by ID
- [ ] [TICKET-026-42] Fetch AIAvatar by ID
- [ ] [TICKET-026-43] Call ForumAIService.generate_response_to_mention()
- [ ] [TICKET-026-44] Create new ForumPost as reply
- [ ] [TICKET-026-45] Set author_avatar to avatar
- [ ] [TICKET-026-46] Save post
- [ ] [TICKET-026-47] Update avatar.last_active_at and post_count
- [ ] [TICKET-026-48] Log success
- [ ] [TICKET-026-49] Handle exceptions and log errors
- [ ] [TICKET-026-50] Create `detect_avatar_mentions()` function with @shared_task
- [ ] [TICKET-026-51] Query recent ForumPosts (last 30 minutes)
- [ ] [TICKET-026-52] Loop through posts and extract mentions
- [ ] [TICKET-026-53] Get mentioned avatars for each post
- [ ] [TICKET-026-54] Check if avatar already responded
- [ ] [TICKET-026-55] Dispatch ai_avatar_respond_to_mention task if not responded
- [ ] [TICKET-026-56] Log dispatched tasks
- [ ] [TICKET-026-57] Return count of dispatched tasks
- [ ] [TICKET-026-58] Add docstrings to tasks

#### Implementation Tasks - Signals
- [ ] [TICKET-026-59] Update `apps/forum/signals.py` to add mention detection
- [ ] [TICKET-026-60] Create `detect_mentions_on_post_save` function with @receiver decorator
- [ ] [TICKET-026-61] Connect to ForumPost post_save signal
- [ ] [TICKET-026-62] Check if instance is newly created
- [ ] [TICKET-026-63] Extract mentions from post content
- [ ] [TICKET-026-64] Get mentioned avatars
- [ ] [TICKET-026-65] Dispatch ai_avatar_respond_to_mention task for each avatar
- [ ] [TICKET-026-66] Add docstring to signal handler

#### Implementation Tasks - Beat Schedule
- [ ] [TICKET-026-67] Update CELERY_BEAT_SCHEDULE in `config/settings/base.py`
- [ ] [TICKET-026-68] Add 'ai-detect-mentions' task entry
- [ ] [TICKET-026-69] Set schedule to crontab(minute='*/30') for every 30 minutes

#### Implementation Tasks - Rate Limiting
- [ ] [TICKET-026-70] Update `apps/forum/utils.py` to add AI rate limiting
- [ ] [TICKET-026-71] Create `check_ai_response_rate_limit(avatar, topic)` function
- [ ] [TICKET-026-72] Build cache key from avatar ID and topic ID
- [ ] [TICKET-026-73] Check if avatar responded in last hour
- [ ] [TICKET-026-74] Return boolean (True if allowed, False if rate limited)
- [ ] [TICKET-026-75] Update ai_avatar_respond_to_mention task to check rate limit

#### Verification Tasks
- [ ] [TICKET-026-76] Create test ForumPost mentioning AI avatar
- [ ] [TICKET-026-77] Verify mention detection signal triggers
- [ ] [TICKET-026-78] Verify AI response task dispatched
- [ ] [TICKET-026-79] Verify AI response post created
- [ ] [TICKET-026-80] Verify conversation context included in response
- [ ] [TICKET-026-81] Test rate limiting by creating multiple mentions
- [ ] [TICKET-026-82] Verify only one response per hour per topic
- [ ] [TICKET-026-83] Run detect_avatar_mentions task manually
- [ ] [TICKET-026-84] Verify mentions detected and tasks dispatched
- [ ] [TICKET-026-85] Run `pytest apps/forum/tests/test_ai_participation.py -v`
- [ ] [TICKET-026-86] Verify all tests pass

---

### TICKET-027: Content Moderation - Keyword and Rule-Based Filtering
**Dependencies:** TICKET-021

#### Test Tasks
- [ ] [TICKET-027-01] Create `apps/moderation/` directory
- [ ] [TICKET-027-02] Create `apps/moderation/__init__.py`
- [ ] [TICKET-027-03] Create `apps/moderation/tests/` directory
- [ ] [TICKET-027-04] Create `apps/moderation/tests/__init__.py`
- [ ] [TICKET-027-05] Create `apps/moderation/tests/test_services.py` with imports
- [ ] [TICKET-027-06] Add `TestModerationRule` test class
- [ ] [TICKET-027-07] Write `test_moderation_rule_creation` test method
- [ ] [TICKET-027-08] Write `test_check_content_keyword` test method
- [ ] [TICKET-027-09] Write `test_check_content_regex` test method
- [ ] [TICKET-027-10] Add `TestModerationService` test class
- [ ] [TICKET-027-11] Write `test_check_content` test method
- [ ] [TICKET-027-12] Write `test_apply_keyword_rules` test method
- [ ] [TICKET-027-13] Write `test_apply_regex_rules` test method
- [ ] [TICKET-027-14] Write `test_determine_action` test method

#### Implementation Tasks - Apps Config
- [ ] [TICKET-027-15] Create `apps/moderation/apps.py` with ModerationConfig class
- [ ] [TICKET-027-16] Set name = 'apps.moderation' in ModerationConfig
- [ ] [TICKET-027-17] Add 'apps.moderation' to INSTALLED_APPS in `config/settings/base.py`

#### Implementation Tasks - Models
- [ ] [TICKET-027-18] Create `apps/moderation/models.py` with imports
- [ ] [TICKET-027-19] Import ContentType, GenericForeignKey
- [ ] [TICKET-027-20] Create RULE_TYPE_CHOICES tuple
- [ ] [TICKET-027-21] Create SEVERITY_CHOICES tuple
- [ ] [TICKET-027-22] Create ACTION_CHOICES tuple
- [ ] [TICKET-027-23] Create `ModerationRule` model class inheriting from TimeStampedModel
- [ ] [TICKET-027-24] Add `name` field (CharField, max_length=100)
- [ ] [TICKET-027-25] Add `rule_type` field (CharField with RULE_TYPE_CHOICES)
- [ ] [TICKET-027-26] Add `pattern` field (TextField)
- [ ] [TICKET-027-27] Add `severity` field (CharField with SEVERITY_CHOICES)
- [ ] [TICKET-027-28] Add `action` field (CharField with ACTION_CHOICES)
- [ ] [TICKET-027-29] Add `is_active` field (BooleanField, default=True, db_index=True)
- [ ] [TICKET-027-30] Implement `check_content(text)` method
- [ ] [TICKET-027-31] Handle keyword matching in check_content()
- [ ] [TICKET-027-32] Handle regex matching in check_content()
- [ ] [TICKET-027-33] Handle length checking in check_content()
- [ ] [TICKET-027-34] Handle link count checking in check_content()
- [ ] [TICKET-027-35] Return boolean match result
- [ ] [TICKET-027-36] Implement `__str__()` method returning name
- [ ] [TICKET-027-37] Add Meta class with db_table = 'moderation_rule'
- [ ] [TICKET-027-38] Add docstrings to ModerationRule model and methods
- [ ] [TICKET-027-39] Create ACTION_CHOICES tuple for ModerationLog
- [ ] [TICKET-027-40] Create `ModerationLog` model class inheriting from models.Model
- [ ] [TICKET-027-41] Add `content_type` field (ForeignKey to ContentType)
- [ ] [TICKET-027-42] Add `object_id` field (PositiveIntegerField)
- [ ] [TICKET-027-43] Add `content_object` field (GenericForeignKey)
- [ ] [TICKET-027-44] Add `action` field (CharField with ACTION_CHOICES)
- [ ] [TICKET-027-45] Add `moderator_user` field (ForeignKey to User, null=True, blank=True)
- [ ] [TICKET-027-46] Add `reason` field (TextField)
- [ ] [TICKET-027-47] Add `details` field (JSONField, default=dict, blank=True)
- [ ] [TICKET-027-48] Add `timestamp` field (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-027-49] Implement `__str__()` method
- [ ] [TICKET-027-50] Add Meta class with db_table = 'moderation_log'
- [ ] [TICKET-027-51] Add ordering = ['-timestamp'] to Meta
- [ ] [TICKET-027-52] Add docstrings to ModerationLog model

#### Implementation Tasks - Services
- [ ] [TICKET-027-53] Create `apps/moderation/services.py` with imports
- [ ] [TICKET-027-54] Import re for regex
- [ ] [TICKET-027-55] Create `ModerationService` class
- [ ] [TICKET-027-56] Implement `check_content(text, content_type='post')` method
- [ ] [TICKET-027-57] Query active ModerationRules
- [ ] [TICKET-027-58] Call apply_keyword_rules(), apply_regex_rules(), etc.
- [ ] [TICKET-027-59] Collect matched rules
- [ ] [TICKET-027-60] Call determine_action() with matched rules
- [ ] [TICKET-027-61] Return action and matched rules
- [ ] [TICKET-027-62] Implement `apply_keyword_rules(text)` method
- [ ] [TICKET-027-63] Query keyword rules
- [ ] [TICKET-027-64] Check each rule against text
- [ ] [TICKET-027-65] Return list of matched rules
- [ ] [TICKET-027-66] Implement `apply_regex_rules(text)` method
- [ ] [TICKET-027-67] Query regex rules
- [ ] [TICKET-027-68] Compile and match each regex
- [ ] [TICKET-027-69] Return list of matched rules
- [ ] [TICKET-027-70] Implement `apply_length_rules(text)` method
- [ ] [TICKET-027-71] Check text length against rules
- [ ] [TICKET-027-72] Return list of matched rules
- [ ] [TICKET-027-73] Implement `apply_link_rules(text)` method
- [ ] [TICKET-027-74] Count links in text
- [ ] [TICKET-027-75] Check against link count rules
- [ ] [TICKET-027-76] Return list of matched rules
- [ ] [TICKET-027-77] Implement `determine_action(matched_rules)` method
- [ ] [TICKET-027-78] Check highest severity in matched rules
- [ ] [TICKET-027-79] Return appropriate action (flag, reject, approve)
- [ ] [TICKET-027-80] Implement `log_moderation(content_object, action, reason, details)` method
- [ ] [TICKET-027-81] Create ModerationLog entry
- [ ] [TICKET-027-82] Save log
- [ ] [TICKET-027-83] Return log instance
- [ ] [TICKET-027-84] Add docstrings to ModerationService and methods

#### Implementation Tasks - Management Command
- [ ] [TICKET-027-85] Create `apps/moderation/management/` directory
- [ ] [TICKET-027-86] Create `apps/moderation/management/__init__.py`
- [ ] [TICKET-027-87] Create `apps/moderation/management/commands/` directory
- [ ] [TICKET-027-88] Create `apps/moderation/management/commands/__init__.py`
- [ ] [TICKET-027-89] Create `apps/moderation/management/commands/create_default_rules.py`
- [ ] [TICKET-027-90] Create Command class
- [ ] [TICKET-027-91] Implement handle() method
- [ ] [TICKET-027-92] Create hate speech keyword rules (critical severity, reject)
- [ ] [TICKET-027-93] Create spam pattern rules (high severity, flag)
- [ ] [TICKET-027-94] Create excessive links rules (medium severity, flag)
- [ ] [TICKET-027-95] Create very short post rules (low severity, flag)
- [ ] [TICKET-027-96] Add output messages showing created rules

#### Implementation Tasks - Tasks
- [ ] [TICKET-027-97] Create `apps/moderation/tasks.py` with imports
- [ ] [TICKET-027-98] Create `moderate_content(content_type, object_id)` function with @shared_task
- [ ] [TICKET-027-99] Fetch content object by content_type and object_id
- [ ] [TICKET-027-100] Extract text content
- [ ] [TICKET-027-101] Call ModerationService.check_content()
- [ ] [TICKET-027-102] Update content moderation_status based on action
- [ ] [TICKET-027-103] Call ModerationService.log_moderation()
- [ ] [TICKET-027-104] Save content object
- [ ] [TICKET-027-105] Log success or errors
- [ ] [TICKET-027-106] Return moderation result
- [ ] [TICKET-027-107] Add docstring to task

#### Implementation Tasks - Signals
- [ ] [TICKET-027-108] Update `apps/forum/signals.py` to trigger moderation
- [ ] [TICKET-027-109] Update update_counts_on_post_save signal handler
- [ ] [TICKET-027-110] Check if MODERATION_ENABLED setting is True
- [ ] [TICKET-027-111] Dispatch moderate_content task asynchronously
- [ ] [TICKET-027-112] Add error handling

#### Settings Tasks
- [ ] [TICKET-027-113] Add MODERATION_ENABLED = True to `config/settings/base.py`
- [ ] [TICKET-027-114] Add MODERATION_AUTO_APPROVE_THRESHOLD = 0.3

#### Admin Tasks
- [ ] [TICKET-027-115] Create `apps/moderation/admin.py` with imports
- [ ] [TICKET-027-116] Create `ModerationRuleAdmin` class
- [ ] [TICKET-027-117] Add list_display (name, rule_type, severity, action, is_active)
- [ ] [TICKET-027-118] Add list_filter (rule_type, severity, action, is_active)
- [ ] [TICKET-027-119] Add search_fields (name, pattern)
- [ ] [TICKET-027-120] Register ModerationRule with ModerationRuleAdmin
- [ ] [TICKET-027-121] Create `ModerationLogAdmin` class
- [ ] [TICKET-027-122] Add list_display (content_object, action, timestamp)
- [ ] [TICKET-027-123] Add list_filter (action, timestamp)
- [ ] [TICKET-027-124] Add readonly_fields (all fields)
- [ ] [TICKET-027-125] Register ModerationLog with ModerationLogAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-027-126] Run `python manage.py makemigrations moderation`
- [ ] [TICKET-027-127] Run `python manage.py migrate`
- [ ] [TICKET-027-128] Run `python manage.py check`
- [ ] [TICKET-027-129] Run `python manage.py create_default_rules`
- [ ] [TICKET-027-130] Verify rules created in database
- [ ] [TICKET-027-131] Create test ForumPost with prohibited content
- [ ] [TICKET-027-132] Verify moderation triggered
- [ ] [TICKET-027-133] Verify post flagged or rejected
- [ ] [TICKET-027-134] Verify ModerationLog entry created
- [ ] [TICKET-027-135] Test keyword rules with various content
- [ ] [TICKET-027-136] Test regex rules
- [ ] [TICKET-027-137] Test length and link rules
- [ ] [TICKET-027-138] Run `pytest apps/moderation/tests/test_services.py -v`
- [ ] [TICKET-027-139] Verify all tests pass

---

### TICKET-028: Content Moderation - AI-Powered Analysis
**Dependencies:** TICKET-027, TICKET-014

#### Test Tasks
- [ ] [TICKET-028-01] Create `apps/moderation/tests/test_ai_moderation.py` with imports
- [ ] [TICKET-028-02] Add `TestAIModeration` test class
- [ ] [TICKET-028-03] Write `test_analyze_toxicity` test method (mocked AI)
- [ ] [TICKET-028-04] Write `test_analyze_spam` test method (mocked AI)
- [ ] [TICKET-028-05] Write `test_get_moderation_scores` test method (mocked AI)
- [ ] [TICKET-028-06] Write `test_should_flag_content` test method
- [ ] [TICKET-028-07] Add `TestModerationViews` test class
- [ ] [TICKET-028-08] Write `test_moderation_queue_view` test method
- [ ] [TICKET-028-09] Write `test_moderation_review_view` test method

#### Implementation Tasks - Prompts
- [ ] [TICKET-028-10] Create `apps/moderation/prompts.py` with imports
- [ ] [TICKET-028-11] Create `TOXICITY_ANALYSIS_PROMPT` template string
- [ ] [TICKET-028-12] Add instructions to analyze toxicity, hate speech, harassment
- [ ] [TICKET-028-13] Add JSON response format instructions (scores 0.0-1.0)
- [ ] [TICKET-028-14] Add category breakdown (toxicity, hate_speech, harassment, profanity)
- [ ] [TICKET-028-15] Create `SPAM_ANALYSIS_PROMPT` template string
- [ ] [TICKET-028-16] Add instructions to analyze spam indicators
- [ ] [TICKET-028-17] Add JSON response format with spam score and reasoning
- [ ] [TICKET-028-18] Add docstrings explaining prompts

#### Implementation Tasks - Services
- [ ] [TICKET-028-19] Update `apps/moderation/services.py` to add AIModeration class
- [ ] [TICKET-028-20] Import AIService, prompts, json
- [ ] [TICKET-028-21] Create `AIModeration` class
- [ ] [TICKET-028-22] Implement `analyze_toxicity(text)` method
- [ ] [TICKET-028-23] Format TOXICITY_ANALYSIS_PROMPT with text
- [ ] [TICKET-028-24] Call AIService.generate_text() with prompt
- [ ] [TICKET-028-25] Parse JSON response
- [ ] [TICKET-028-26] Return toxicity scores dictionary
- [ ] [TICKET-028-27] Implement `analyze_spam(text)` method
- [ ] [TICKET-028-28] Format SPAM_ANALYSIS_PROMPT with text
- [ ] [TICKET-028-29] Call AIService.generate_text() with prompt
- [ ] [TICKET-028-30] Parse JSON response
- [ ] [TICKET-028-31] Return spam score and reasoning
- [ ] [TICKET-028-32] Implement `analyze_sentiment(text)` method (optional)
- [ ] [TICKET-028-33] Implement `get_moderation_scores(text)` method
- [ ] [TICKET-028-34] Call analyze_toxicity() and analyze_spam()
- [ ] [TICKET-028-35] Combine all scores into single dictionary
- [ ] [TICKET-028-36] Return combined scores
- [ ] [TICKET-028-37] Implement `should_flag_content(scores)` method
- [ ] [TICKET-028-38] Check scores against thresholds from settings
- [ ] [TICKET-028-39] Return boolean decision and reason
- [ ] [TICKET-028-40] Add error handling for AI failures
- [ ] [TICKET-028-41] Add docstrings to AIModeration and methods

#### Implementation Tasks - Tasks
- [ ] [TICKET-028-42] Update `apps/moderation/tasks.py` moderate_content task
- [ ] [TICKET-028-43] After keyword/rule checks, check if MODERATION_AI_ENABLED
- [ ] [TICKET-028-44] If enabled and passed rule checks, run AI analysis
- [ ] [TICKET-028-45] Call AIModeration.get_moderation_scores()
- [ ] [TICKET-028-46] Call AIModeration.should_flag_content()
- [ ] [TICKET-028-47] Update moderation_status based on AI decision
- [ ] [TICKET-028-48] Log AI scores in moderation_details
- [ ] [TICKET-028-49] Update ModerationLog with AI scores

#### Settings Tasks
- [ ] [TICKET-028-50] Add MODERATION_AI_ENABLED = True to `config/settings/base.py`
- [ ] [TICKET-028-51] Add MODERATION_TOXICITY_THRESHOLD = 0.7
- [ ] [TICKET-028-52] Add MODERATION_SPAM_THRESHOLD = 0.8
- [ ] [TICKET-028-53] Add MODERATION_AUTO_REJECT_THRESHOLD = 0.9

#### Implementation Tasks - Views
- [ ] [TICKET-028-54] Create `apps/moderation/views.py` with imports
- [ ] [TICKET-028-55] Import PermissionRequiredMixin
- [ ] [TICKET-028-56] Create `ModerationQueueView` class inheriting from PermissionRequiredMixin, ListView
- [ ] [TICKET-028-57] Set permission_required = 'moderation.view_moderationlog'
- [ ] [TICKET-028-58] Set model = ModerationLog
- [ ] [TICKET-028-59] Set template_name = 'moderation/queue.html'
- [ ] [TICKET-028-60] Set context_object_name = 'logs'
- [ ] [TICKET-028-61] Set paginate_by = 50
- [ ] [TICKET-028-62] Override get_queryset() to filter flagged content
- [ ] [TICKET-028-63] Order by timestamp descending
- [ ] [TICKET-028-64] Create `ModerationReviewView` class inheriting from PermissionRequiredMixin, DetailView
- [ ] [TICKET-028-65] Set permission_required = 'moderation.change_moderationlog'
- [ ] [TICKET-028-66] Set model = ModerationLog
- [ ] [TICKET-028-67] Set template_name = 'moderation/review_detail.html'
- [ ] [TICKET-028-68] Override get_context_data() to add content object
- [ ] [TICKET-028-69] Add moderation history for content
- [ ] [TICKET-028-70] Add action form to context
- [ ] [TICKET-028-71] Implement post() method to handle approve/reject actions
- [ ] [TICKET-028-72] Update content moderation_status
- [ ] [TICKET-028-73] Create new ModerationLog entry
- [ ] [TICKET-028-74] Redirect with success message
- [ ] [TICKET-028-75] Add docstrings to views

#### Implementation Tasks - Templates
- [ ] [TICKET-028-76] Create `apps/moderation/templates/` directory
- [ ] [TICKET-028-77] Create `apps/moderation/templates/moderation/` directory
- [ ] [TICKET-028-78] Create `apps/moderation/templates/moderation/queue.html` extending base.html
- [ ] [TICKET-028-79] Add page title "Moderation Queue"
- [ ] [TICKET-028-80] Create table with flagged content
- [ ] [TICKET-028-81] Display content preview, author, AI scores
- [ ] [TICKET-028-82] Display matched rules
- [ ] [TICKET-028-83] Add action buttons (review, approve, reject)
- [ ] [TICKET-028-84] Add pagination controls
- [ ] [TICKET-028-85] Create `apps/moderation/templates/moderation/review_detail.html` extending base.html
- [ ] [TICKET-028-86] Add page title "Review Content"
- [ ] [TICKET-028-87] Display full content
- [ ] [TICKET-028-88] Display AI moderation scores with visual indicators
- [ ] [TICKET-028-89] Display matched rules
- [ ] [TICKET-028-90] Display moderation history
- [ ] [TICKET-028-91] Add action form with approve/reject buttons
- [ ] [TICKET-028-92] Add reason textarea for moderator notes

#### Implementation Tasks - URLs
- [ ] [TICKET-028-93] Create `apps/moderation/urls.py` with imports
- [ ] [TICKET-028-94] Set app_name = 'moderation'
- [ ] [TICKET-028-95] Add URL pattern for ModerationQueueView (path '', name='queue')
- [ ] [TICKET-028-96] Add URL pattern for ModerationReviewView (path '<int:pk>/', name='review')
- [ ] [TICKET-028-97] Update `config/urls.py` to include moderation.urls at 'moderation/'

#### Permissions Tasks
- [ ] [TICKET-028-98] Create "Moderators" group via Django admin or data migration
- [ ] [TICKET-028-99] Assign moderation permissions to group

#### Verification Tasks
- [ ] [TICKET-028-100] Create test ForumPost with toxic content
- [ ] [TICKET-028-101] Verify AI moderation triggered
- [ ] [TICKET-028-102] Verify toxicity scores calculated
- [ ] [TICKET-028-103] Verify content flagged if above threshold
- [ ] [TICKET-028-104] Access moderation queue as moderator
- [ ] [TICKET-028-105] Verify flagged content appears in queue
- [ ] [TICKET-028-106] Click review on flagged content
- [ ] [TICKET-028-107] Verify AI scores displayed
- [ ] [TICKET-028-108] Approve content and verify status updated
- [ ] [TICKET-028-109] Test reject action
- [ ] [TICKET-028-110] Run `pytest apps/moderation/tests/test_ai_moderation.py -v`
- [ ] [TICKET-028-111] Verify all tests pass with mocked AI

---

### TICKET-029: Testing and Documentation
**Dependencies:** All previous tickets

#### Test Tasks - Integration Tests
- [ ] [TICKET-029-01] Create `tests/` directory in project root
- [ ] [TICKET-029-02] Create `tests/__init__.py`
- [ ] [TICKET-029-03] Create `tests/integration/` directory
- [ ] [TICKET-029-04] Create `tests/integration/__init__.py`
- [ ] [TICKET-029-05] Create `tests/integration/test_content_pipeline.py`
- [ ] [TICKET-029-06] Write test for full content aggregation → processing → display flow
- [ ] [TICKET-029-07] Create `tests/integration/test_ai_generation.py`
- [ ] [TICKET-029-08] Write test for AI article generation → publication flow
- [ ] [TICKET-029-09] Create `tests/integration/test_user_forum_flow.py`
- [ ] [TICKET-029-10] Write test for user registration → forum participation flow
- [ ] [TICKET-029-11] Create `tests/integration/test_ai_avatar_participation.py`
- [ ] [TICKET-029-12] Write test for AI avatar topic initiation and response flow
- [ ] [TICKET-029-13] Create `tests/integration/test_moderation_flow.py`
- [ ] [TICKET-029-14] Write test for content moderation pipeline

#### Test Tasks - Factory Classes
- [ ] [TICKET-029-15] Review all apps for factory classes
- [ ] [TICKET-029-16] Ensure all models have corresponding factories
- [ ] [TICKET-029-17] Add realistic test data to factories
- [ ] [TICKET-029-18] Add support for related objects in factories

#### Test Tasks - Coverage
- [ ] [TICKET-029-19] Create `pytest.ini` in project root
- [ ] [TICKET-029-20] Configure test database settings
- [ ] [TICKET-029-21] Configure coverage reporting
- [ ] [TICKET-029-22] Set coverage minimum threshold to 80%
- [ ] [TICKET-029-23] Configure test markers (unit, integration, slow)
- [ ] [TICKET-029-24] Add pytest-cov to requirements/testing.txt
- [ ] [TICKET-029-25] Add pytest-django to requirements/testing.txt
- [ ] [TICKET-029-26] Add pytest-mock to requirements/testing.txt

#### Documentation Tasks - README
- [ ] [TICKET-029-27] Update `README.md` with project overview
- [ ] [TICKET-029-28] Add features list to README
- [ ] [TICKET-029-29] Add technology stack section
- [ ] [TICKET-029-30] Add architecture diagram (ASCII or link to image)
- [ ] [TICKET-029-31] Add setup instructions for local development
- [ ] [TICKET-029-32] Add setup instructions for Docker
- [ ] [TICKET-029-33] Add environment variables documentation
- [ ] [TICKET-029-34] Add running tests section
- [ ] [TICKET-029-35] Add deployment guide overview
- [ ] [TICKET-029-36] Add contributing guidelines
- [ ] [TICKET-029-37] Add license information

#### Documentation Tasks - Detailed Docs
- [ ] [TICKET-029-38] Create `docs/` directory
- [ ] [TICKET-029-39] Create `docs/ARCHITECTURE.md`
- [ ] [TICKET-029-40] Document system architecture in ARCHITECTURE.md
- [ ] [TICKET-029-41] Add component diagrams
- [ ] [TICKET-029-42] Document data flow
- [ ] [TICKET-029-43] Document technology choices and rationale
- [ ] [TICKET-029-44] Create `docs/API.md`
- [ ] [TICKET-029-45] Document internal API endpoints (if any)
- [ ] [TICKET-029-46] Document key service classes and methods
- [ ] [TICKET-029-47] Add usage examples
- [ ] [TICKET-029-48] Create `docs/DEPLOYMENT.md`
- [ ] [TICKET-029-49] Document production deployment steps
- [ ] [TICKET-029-50] Document environment configuration
- [ ] [TICKET-029-51] Document database setup and migrations
- [ ] [TICKET-029-52] Document Celery worker and beat setup
- [ ] [TICKET-029-53] Document monitoring and logging setup
- [ ] [TICKET-029-54] Create `docs/DEVELOPMENT.md`
- [ ] [TICKET-029-55] Document development environment setup
- [ ] [TICKET-029-56] Document coding standards
- [ ] [TICKET-029-57] Document testing guidelines
- [ ] [TICKET-029-58] Document Git workflow
- [ ] [TICKET-029-59] Create `docs/MODERATION.md`
- [ ] [TICKET-029-60] Document moderation guidelines
- [ ] [TICKET-029-61] Document moderation workflow
- [ ] [TICKET-029-62] Document AI moderation configuration

#### Docstring Tasks
- [ ] [TICKET-029-63] Review all model classes and add/update docstrings
- [ ] [TICKET-029-64] Review all view classes and add/update docstrings
- [ ] [TICKET-029-65] Review all service classes and add/update docstrings
- [ ] [TICKET-029-66] Review all task functions and add/update docstrings
- [ ] [TICKET-029-67] Review all utility functions and add/update docstrings
- [ ] [TICKET-029-68] Ensure docstrings follow Google or NumPy style

#### Management Command Tasks
- [ ] [TICKET-029-69] Create `apps/core/management/commands/system_check.py`
- [ ] [TICKET-029-70] Create Command class
- [ ] [TICKET-029-71] Implement handle() method
- [ ] [TICKET-029-72] Check database connectivity
- [ ] [TICKET-029-73] Check Redis connectivity
- [ ] [TICKET-029-74] Check Celery workers status
- [ ] [TICKET-029-75] Verify AI API keys configured
- [ ] [TICKET-029-76] Check for pending migrations
- [ ] [TICKET-029-77] Display system health report
- [ ] [TICKET-029-78] Add color-coded output (green/yellow/red)

#### Verification Tasks
- [ ] [TICKET-029-79] Run `pytest --cov=apps --cov-report=html`
- [ ] [TICKET-029-80] Verify coverage >80% for all apps
- [ ] [TICKET-029-81] Review coverage report and add tests for uncovered code
- [ ] [TICKET-029-82] Run all integration tests
- [ ] [TICKET-029-83] Verify all integration tests pass
- [ ] [TICKET-029-84] Run `python manage.py system_check`
- [ ] [TICKET-029-85] Verify all system checks pass
- [ ] [TICKET-029-86] Review all documentation for completeness
- [ ] [TICKET-029-87] Test all documented setup procedures
- [ ] [TICKET-029-88] Verify README instructions work for new developer

---

### TICKET-030: Production Deployment Configuration
**Dependencies:** TICKET-029

#### Test Tasks
- [ ] [TICKET-030-01] Create `tests/deployment/` directory
- [ ] [TICKET-030-02] Create `tests/deployment/test_settings.py`
- [ ] [TICKET-030-03] Write tests for production settings validation
- [ ] [TICKET-030-04] Write tests for security settings

#### Implementation Tasks - Production Settings
- [ ] [TICKET-030-05] Update `config/settings/production.py` to set DEBUG = False
- [ ] [TICKET-030-06] Configure ALLOWED_HOSTS from environment variable
- [ ] [TICKET-030-07] Set SECURE_SSL_REDIRECT = True
- [ ] [TICKET-030-08] Set SESSION_COOKIE_SECURE = True
- [ ] [TICKET-030-09] Set CSRF_COOKIE_SECURE = True
- [ ] [TICKET-030-10] Set SECURE_HSTS_SECONDS = 31536000 (1 year)
- [ ] [TICKET-030-11] Set SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- [ ] [TICKET-030-12] Set SECURE_HSTS_PRELOAD = True
- [ ] [TICKET-030-13] Set SECURE_CONTENT_TYPE_NOSNIFF = True
- [ ] [TICKET-030-14] Set SECURE_BROWSER_XSS_FILTER = True
- [ ] [TICKET-030-15] Set X_FRAME_OPTIONS = 'DENY'
- [ ] [TICKET-030-16] Configure database connection pooling
- [ ] [TICKET-030-17] Configure static file serving with WhiteNoise
- [ ] [TICKET-030-18] Add WhiteNoise to MIDDLEWARE
- [ ] [TICKET-030-19] Set STATICFILES_STORAGE to WhiteNoise storage
- [ ] [TICKET-030-20] Configure logging to file and Sentry
- [ ] [TICKET-030-21] Add Sentry DSN from environment
- [ ] [TICKET-030-22] Configure log levels (INFO for production)
- [ ] [TICKET-030-23] Add log rotation configuration

#### Implementation Tasks - Docker Production
- [ ] [TICKET-030-24] Create `docker-compose.prod.yml`
- [ ] [TICKET-030-25] Configure web service with gunicorn
- [ ] [TICKET-030-26] Set gunicorn workers and threads
- [ ] [TICKET-030-27] Configure nginx service
- [ ] [TICKET-030-28] Set resource limits for all services
- [ ] [TICKET-030-29] Configure health checks for all services
- [ ] [TICKET-030-30] Configure restart policies
- [ ] [TICKET-030-31] Configure volumes for persistent data
- [ ] [TICKET-030-32] Configure networks for service isolation

#### Implementation Tasks - Nginx
- [ ] [TICKET-030-33] Create `docker/nginx.conf`
- [ ] [TICKET-030-34] Configure upstream to Django application
- [ ] [TICKET-030-35] Configure server block for HTTP (redirect to HTTPS)
- [ ] [TICKET-030-36] Configure server block for HTTPS
- [ ] [TICKET-030-37] Configure SSL certificate paths
- [ ] [TICKET-030-38] Configure static file serving
- [ ] [TICKET-030-39] Configure media file serving
- [ ] [TICKET-030-40] Add security headers
- [ ] [TICKET-030-41] Configure gzip compression
- [ ] [TICKET-030-42] Configure rate limiting
- [ ] [TICKET-030-43] Configure client max body size

#### Implementation Tasks - Deployment Scripts
- [ ] [TICKET-030-44] Create `scripts/deploy.sh`
- [ ] [TICKET-030-45] Add git pull command
- [ ] [TICKET-030-46] Add docker-compose build command
- [ ] [TICKET-030-47] Add database migration command
- [ ] [TICKET-030-48] Add collectstatic command
- [ ] [TICKET-030-49] Add docker-compose up command
- [ ] [TICKET-030-50] Add health check after deployment
- [ ] [TICKET-030-51] Add rollback logic on failure
- [ ] [TICKET-030-52] Create `scripts/backup_db.sh`
- [ ] [TICKET-030-53] Add pg_dump command with timestamp
- [ ] [TICKET-030-54] Add compression
- [ ] [TICKET-030-55] Add upload to backup storage (S3 or similar)
- [ ] [TICKET-030-56] Create `scripts/restore_db.sh`
- [ ] [TICKET-030-57] Add download from backup storage
- [ ] [TICKET-030-58] Add pg_restore command
- [ ] [TICKET-030-59] Add verification step

#### Implementation Tasks - Health Checks
- [ ] [TICKET-030-60] Create `apps/core/views.py` health check views
- [ ] [TICKET-030-61] Create `health_check()` view
- [ ] [TICKET-030-62] Return JSON with status: ok
- [ ] [TICKET-030-63] Create `health_check_db()` view
- [ ] [TICKET-030-64] Test database connectivity
- [ ] [TICKET-030-65] Return JSON with database status
- [ ] [TICKET-030-66] Create `health_check_redis()` view
- [ ] [TICKET-030-67] Test Redis connectivity
- [ ] [TICKET-030-68] Return JSON with Redis status
- [ ] [TICKET-030-69] Create `health_check_celery()` view
- [ ] [TICKET-030-70] Check Celery worker status
- [ ] [TICKET-030-71] Return JSON with Celery status
- [ ] [TICKET-030-72] Add URL patterns for health checks

#### Environment Configuration Tasks
- [ ] [TICKET-030-73] Update `.env.example` with all production variables
- [ ] [TICKET-030-74] Add SECRET_KEY generation instructions
- [ ] [TICKET-030-75] Add database URL format
- [ ] [TICKET-030-76] Add Redis URL format
- [ ] [TICKET-030-77] Add email configuration variables
- [ ] [TICKET-030-78] Add Sentry DSN variable
- [ ] [TICKET-030-79] Add allowed hosts variable
- [ ] [TICKET-030-80] Add SSL certificate paths

#### Security Checklist Tasks
- [ ] [TICKET-030-81] Run `python manage.py check --deploy`
- [ ] [TICKET-030-82] Fix all security warnings
- [ ] [TICKET-030-83] Review and configure CORS if needed
- [ ] [TICKET-030-84] Configure CSP headers
- [ ] [TICKET-030-85] Review file upload security
- [ ] [TICKET-030-86] Review authentication security
- [ ] [TICKET-030-87] Review API rate limiting
- [ ] [TICKET-030-88] Review database security (SSL, passwords)

#### Monitoring Configuration Tasks
- [ ] [TICKET-030-89] Configure Sentry for error tracking
- [ ] [TICKET-030-90] Test Sentry integration
- [ ] [TICKET-030-91] Configure Celery monitoring with Flower
- [ ] [TICKET-030-92] Secure Flower with authentication
- [ ] [TICKET-030-93] Configure application performance monitoring (optional)

#### Documentation Tasks
- [ ] [TICKET-030-94] Update `docs/DEPLOYMENT.md` with production steps
- [ ] [TICKET-030-95] Document environment variables
- [ ] [TICKET-030-96] Document SSL certificate setup
- [ ] [TICKET-030-97] Document backup and restore procedures
- [ ] [TICKET-030-98] Document monitoring setup
- [ ] [TICKET-030-99] Document troubleshooting common issues

#### Verification Tasks
- [ ] [TICKET-030-100] Test production Docker Compose build
- [ ] [TICKET-030-101] Test deployment script in staging environment
- [ ] [TICKET-030-102] Verify all services start correctly
- [ ] [TICKET-030-103] Access health check endpoints
- [ ] [TICKET-030-104] Verify all health checks pass
- [ ] [TICKET-030-105] Test SSL configuration
- [ ] [TICKET-030-106] Test static file serving
- [ ] [TICKET-030-107] Test media file serving
- [ ] [TICKET-030-108] Run security check and verify all pass
- [ ] [TICKET-030-109] Test backup script
- [ ] [TICKET-030-110] Test restore script
- [ ] [TICKET-030-111] Verify Sentry error tracking works
- [ ] [TICKET-030-112] Load test application (optional)
- [ ] [TICKET-030-113] Document any production-specific configurations

---

---

### TICKET-031: Automated Source Discovery and Vetting System
**Dependencies:** TICKET-009, TICKET-010

#### Test Tasks
- [ ] [TICKET-031-01] Create `apps/aggregation/tests/test_discovery.py` with imports
- [ ] [TICKET-031-02] Add `TestSourceDiscovery` test class
- [ ] [TICKET-031-03] Write `test_source_discovery_creation` test method
- [ ] [TICKET-031-04] Write `test_calculate_relevance_score` test method
- [ ] [TICKET-031-05] Write `test_calculate_quality_score` test method
- [ ] [TICKET-031-06] Write `test_check_for_rss_feed` test method
- [ ] [TICKET-031-07] Write `test_promote_to_source` test method
- [ ] [TICKET-031-08] Add `TestDiscoveryService` test class
- [ ] [TICKET-031-09] Write `test_discover_from_search_api` test method (mocked)
- [ ] [TICKET-031-10] Write `test_analyze_discovered_source` test method
- [ ] [TICKET-031-11] Write `test_auto_vet_source` test method (mocked AI)

#### Implementation Tasks - Model
- [ ] [TICKET-031-12] Update `apps/aggregation/models.py` to add SourceDiscovery model
- [ ] [TICKET-031-13] Add `url` field (URLField, unique=True, db_index=True)
- [ ] [TICKET-031-14] Add `discovered_via` field (CharField with choices)
- [ ] [TICKET-031-15] Add `discovered_at` field (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-031-16] Add `relevance_score` field (FloatField, default=0.0)
- [ ] [TICKET-031-17] Add `quality_score` field (FloatField, default=0.0)
- [ ] [TICKET-031-18] Add `has_rss_feed` field (BooleanField, default=False)
- [ ] [TICKET-031-19] Add `rss_feed_url` field (URLField, null=True, blank=True)
- [ ] [TICKET-031-20] Add `has_api` field (BooleanField, default=False)
- [ ] [TICKET-031-21] Add `api_endpoint` field (URLField, null=True, blank=True)
- [ ] [TICKET-031-22] Add `content_sample` field (TextField, blank=True)
- [ ] [TICKET-031-23] Add `metadata` field (JSONField, default=dict)
- [ ] [TICKET-031-24] Add `vetting_status` field (CharField with choices, db_index=True)
- [ ] [TICKET-031-25] Add `vetting_notes` field (TextField, blank=True)
- [ ] [TICKET-031-26] Add `vetted_by` field (ForeignKey to User, null=True)
- [ ] [TICKET-031-27] Add `vetted_at` field (DateTimeField, null=True)
- [ ] [TICKET-031-28] Add `promoted_to_source` field (BooleanField, default=False, db_index=True)
- [ ] [TICKET-031-29] Add `promoted_source` field (ForeignKey to Source, null=True)
- [ ] [TICKET-031-30] Implement `calculate_relevance_score()` method
- [ ] [TICKET-031-31] Implement `calculate_quality_score()` method
- [ ] [TICKET-031-32] Implement `check_for_rss_feed()` method
- [ ] [TICKET-031-33] Implement `check_for_api()` method
- [ ] [TICKET-031-34] Implement `promote_to_source()` method
- [ ] [TICKET-031-35] Add `__str__()` method
- [ ] [TICKET-031-36] Add Meta class with db_table and indexes
- [ ] [TICKET-031-37] Add docstrings to model and methods

#### Implementation Tasks - Discovery Service
- [ ] [TICKET-031-38] Create `apps/aggregation/services/discovery_service.py`
- [ ] [TICKET-031-39] Import necessary modules (requests, feedparser, etc.)
- [ ] [TICKET-031-40] Create `SourceDiscoveryService` class
- [ ] [TICKET-031-41] Implement `discover_from_existing_sources()` method
- [ ] [TICKET-031-42] Implement `discover_from_search_api(query, region)` method
- [ ] [TICKET-031-43] Implement `discover_from_sitemap(domain)` method
- [ ] [TICKET-031-44] Implement `analyze_discovered_source(discovery)` method
- [ ] [TICKET-031-45] Implement `check_rss_feed(url)` method
- [ ] [TICKET-031-46] Implement `extract_content_sample(url)` method
- [ ] [TICKET-031-47] Implement `calculate_relevance(content_sample, metadata)` method
- [ ] [TICKET-031-48] Implement `calculate_quality(content_sample, metadata)` method
- [ ] [TICKET-031-49] Implement `auto_vet_source(discovery)` method
- [ ] [TICKET-031-50] Implement `promote_approved_sources()` method
- [ ] [TICKET-031-51] Add error handling and logging
- [ ] [TICKET-031-52] Add docstrings to all methods

#### Implementation Tasks - Discovery Spiders
- [ ] [TICKET-031-53] Create `scrapers/buxmax_scraper/spiders/discovery_spider.py`
- [ ] [TICKET-031-54] Create `SourceDiscoverySpider` class
- [ ] [TICKET-031-55] Configure spider name and allowed_domains
- [ ] [TICKET-031-56] Implement start_requests() to crawl aggregators
- [ ] [TICKET-031-57] Implement parse() to extract potential source URLs
- [ ] [TICKET-031-58] Implement parse_sitemap() method
- [ ] [TICKET-031-59] Create `SearchAPIDiscoverySpider` class
- [ ] [TICKET-031-60] Integrate Google Custom Search JSON API
- [ ] [TICKET-031-61] Implement search queries for frugal living keywords
- [ ] [TICKET-031-62] Parse search results and extract URLs
- [ ] [TICKET-031-63] Store metadata from API responses
- [ ] [TICKET-031-64] Add docstrings to spiders

#### Implementation Tasks - AI Vetting
- [ ] [TICKET-031-65] Update `apps/aggregation/prompts.py` to add SOURCE_VETTING_PROMPT
- [ ] [TICKET-031-66] Create prompt template for content relevance analysis
- [ ] [TICKET-031-67] Add instructions for quality assessment
- [ ] [TICKET-031-68] Add JSON response format specification
- [ ] [TICKET-031-69] Update SourceDiscoveryService to use AI vetting
- [ ] [TICKET-031-70] Call AIService with vetting prompt
- [ ] [TICKET-031-71] Parse AI response and update scores

#### Implementation Tasks - Tasks
- [ ] [TICKET-031-72] Update `apps/aggregation/tasks.py` to add discovery tasks
- [ ] [TICKET-031-73] Create `discover_sources_from_search(query, region)` task
- [ ] [TICKET-031-74] Create `discover_sources_from_existing()` task
- [ ] [TICKET-031-75] Create `analyze_pending_discoveries()` task
- [ ] [TICKET-031-76] Create `auto_vet_discoveries()` task
- [ ] [TICKET-031-77] Create `promote_approved_discoveries()` task
- [ ] [TICKET-031-78] Add error handling and logging to all tasks
- [ ] [TICKET-031-79] Add docstrings to tasks

#### Implementation Tasks - Celery Beat Schedule
- [ ] [TICKET-031-80] Update CELERY_BEAT_SCHEDULE in `config/settings/base.py`
- [ ] [TICKET-031-81] Add 'discover-sources-search' task (weekly)
- [ ] [TICKET-031-82] Add 'discover-sources-existing' task (daily)
- [ ] [TICKET-031-83] Add 'analyze-discoveries' task (every 6 hours)
- [ ] [TICKET-031-84] Add 'auto-vet-discoveries' task (every 12 hours)
- [ ] [TICKET-031-85] Add 'promote-discoveries' task (daily)

#### Implementation Tasks - Admin
- [ ] [TICKET-031-86] Update `apps/aggregation/admin.py` to add SourceDiscoveryAdmin
- [ ] [TICKET-031-87] Add list_display fields
- [ ] [TICKET-031-88] Add list_filter options
- [ ] [TICKET-031-89] Add search_fields
- [ ] [TICKET-031-90] Create `approve_sources` admin action
- [ ] [TICKET-031-91] Create `reject_sources` admin action
- [ ] [TICKET-031-92] Create `analyze_sources` admin action
- [ ] [TICKET-031-93] Create `promote_to_active_sources` admin action
- [ ] [TICKET-031-94] Register SourceDiscovery with SourceDiscoveryAdmin

#### Implementation Tasks - Dashboard
- [ ] [TICKET-031-95] Create `apps/aggregation/views/discovery_views.py`
- [ ] [TICKET-031-96] Create `DiscoveryQueueView` class
- [ ] [TICKET-031-97] Implement get_queryset() to filter pending discoveries
- [ ] [TICKET-031-98] Implement get_context_data() to add statistics
- [ ] [TICKET-031-99] Create `apps/aggregation/templates/aggregation/discovery_queue.html`
- [ ] [TICKET-031-100] Display pending discoveries table
- [ ] [TICKET-031-101] Show relevance and quality scores
- [ ] [TICKET-031-102] Add approve/reject/needs_review buttons
- [ ] [TICKET-031-103] Add filters for score ranges and discovery method
- [ ] [TICKET-031-104] Update `apps/aggregation/urls.py` to add discovery queue URL

#### Settings Tasks
- [ ] [TICKET-031-105] Add GOOGLE_SEARCH_API_KEY to `config/settings/base.py`
- [ ] [TICKET-031-106] Add SOURCE_DISCOVERY_ENABLED = True
- [ ] [TICKET-031-107] Add AUTO_VETTING_THRESHOLD = 0.7
- [ ] [TICKET-031-108] Update `.env.example` with GOOGLE_SEARCH_API_KEY

#### Migration and Verification Tasks
- [ ] [TICKET-031-109] Run `python manage.py makemigrations aggregation`
- [ ] [TICKET-031-110] Run `python manage.py migrate`
- [ ] [TICKET-031-111] Run `python manage.py check`
- [ ] [TICKET-031-112] Test discover_sources_from_search task manually
- [ ] [TICKET-031-113] Verify SourceDiscovery records created
- [ ] [TICKET-031-114] Test analyze_pending_discoveries task
- [ ] [TICKET-031-115] Verify scores calculated correctly
- [ ] [TICKET-031-116] Test auto_vet_discoveries with AI
- [ ] [TICKET-031-117] Verify high-scoring sources approved
- [ ] [TICKET-031-118] Test promote_approved_discoveries task
- [ ] [TICKET-031-119] Verify Source records created from approved discoveries
- [ ] [TICKET-031-120] Access discovery queue dashboard
- [ ] [TICKET-031-121] Test approve/reject actions
- [ ] [TICKET-031-122] Run `pytest apps/aggregation/tests/test_discovery.py -v`
- [ ] [TICKET-031-123] Verify all tests pass

---

### TICKET-032: Advanced Scraping with JavaScript Rendering and Anti-Detection
**Dependencies:** TICKET-008, TICKET-009

#### Test Tasks
- [ ] [TICKET-032-01] Create `scrapers/buxmax_scraper/tests/test_playwright_spider.py` with imports
- [ ] [TICKET-032-02] Add `TestPlaywrightSpider` test class
- [ ] [TICKET-032-03] Write `test_playwright_spider_initialization` test method
- [ ] [TICKET-032-04] Write `test_wait_for_element` test method (mocked)
- [ ] [TICKET-032-05] Write `test_scroll_to_bottom` test method (mocked)
- [ ] [TICKET-032-06] Write `test_extract_after_js_render` test method (mocked)
- [ ] [TICKET-032-07] Add `TestStealthMiddleware` test class
- [ ] [TICKET-032-08] Write `test_user_agent_rotation` test method
- [ ] [TICKET-032-09] Write `test_request_delay_randomization` test method
- [ ] [TICKET-032-10] Write `test_captcha_detection` test method

#### Implementation Tasks - Dependencies
- [ ] [TICKET-032-11] Add `playwright>=1.40.0` to `requirements/base.txt`
- [ ] [TICKET-032-12] Add `scrapy-playwright>=0.0.34` to `requirements/base.txt`
- [ ] [TICKET-032-13] Add `curl-cffi>=0.6.0` to `requirements/base.txt`
- [ ] [TICKET-032-14] Create `scripts/install_playwright.sh`
- [ ] [TICKET-032-15] Add shebang and playwright install commands to script
- [ ] [TICKET-032-16] Make script executable
- [ ] [TICKET-032-17] Run `playwright install chromium`

#### Implementation Tasks - Scrapy Configuration
- [ ] [TICKET-032-18] Update `scrapers/buxmax_scraper/settings.py`
- [ ] [TICKET-032-19] Add DOWNLOAD_HANDLERS for playwright
- [ ] [TICKET-032-20] Set TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
- [ ] [TICKET-032-21] Set PLAYWRIGHT_BROWSER_TYPE = 'chromium'
- [ ] [TICKET-032-22] Configure PLAYWRIGHT_LAUNCH_OPTIONS with headless=True
- [ ] [TICKET-032-23] Add '--disable-blink-features=AutomationControlled' to args
- [ ] [TICKET-032-24] Set PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 30000
- [ ] [TICKET-032-25] Configure PLAYWRIGHT_CONTEXTS with stealth settings
- [ ] [TICKET-032-26] Add viewport settings to contexts
- [ ] [TICKET-032-27] Add user_agent to contexts

#### Implementation Tasks - Playwright Base Spider
- [ ] [TICKET-032-28] Create `scrapers/buxmax_scraper/spiders/base_playwright_spider.py`
- [ ] [TICKET-032-29] Import scrapy and playwright modules
- [ ] [TICKET-032-30] Create `PlaywrightSpider` base class inheriting from scrapy.Spider
- [ ] [TICKET-032-31] Add custom_settings with playwright enabled
- [ ] [TICKET-032-32] Implement `start_requests()` with playwright meta
- [ ] [TICKET-032-33] Implement `wait_for_element(selector, timeout=10000)` method
- [ ] [TICKET-032-34] Implement `scroll_to_bottom(max_scrolls=10)` method
- [ ] [TICKET-032-35] Add scroll delay logic
- [ ] [TICKET-032-36] Check for scroll completion
- [ ] [TICKET-032-37] Implement `click_load_more_button(selector)` method
- [ ] [TICKET-032-38] Add wait after click
- [ ] [TICKET-032-39] Implement `extract_after_js_render()` method
- [ ] [TICKET-032-40] Add screenshot capability for debugging
- [ ] [TICKET-032-41] Add docstrings to all methods

#### Implementation Tasks - JavaScript Spiders
- [ ] [TICKET-032-42] Create `scrapers/buxmax_scraper/spiders/js_blog_spider.py`
- [ ] [TICKET-032-43] Create `JavaScriptBlogSpider` class inheriting from PlaywrightSpider
- [ ] [TICKET-032-44] Set spider name and allowed_domains
- [ ] [TICKET-032-45] Implement start_requests() with playwright meta
- [ ] [TICKET-032-46] Implement parse() to wait for content
- [ ] [TICKET-032-47] Extract article data after JavaScript execution
- [ ] [TICKET-032-48] Handle lazy-loaded images
- [ ] [TICKET-032-49] Create `scrapers/buxmax_scraper/spiders/js_forum_spider.py`
- [ ] [TICKET-032-50] Create `JavaScriptForumSpider` class
- [ ] [TICKET-032-51] Implement infinite scroll handling
- [ ] [TICKET-032-52] Implement "Load More" button clicking
- [ ] [TICKET-032-53] Extract dynamically loaded posts
- [ ] [TICKET-032-54] Add docstrings to both spiders

#### Implementation Tasks - Stealth Middleware
- [ ] [TICKET-032-55] Create `scrapers/buxmax_scraper/middlewares/stealth_middleware.py`
- [ ] [TICKET-032-56] Import necessary modules
- [ ] [TICKET-032-57] Create `StealthMiddleware` class
- [ ] [TICKET-032-58] Implement `__init__()` to load user agent pool
- [ ] [TICKET-032-59] Implement `process_request()` method
- [ ] [TICKET-032-60] Rotate user agents from pool
- [ ] [TICKET-032-61] Add realistic browser headers
- [ ] [TICKET-032-62] Randomize request delays (1-5 seconds)
- [ ] [TICKET-032-63] Add Accept-Language header
- [ ] [TICKET-032-64] Add Accept-Encoding header
- [ ] [TICKET-032-65] Add Connection header
- [ ] [TICKET-032-66] Implement proxy rotation (if configured)
- [ ] [TICKET-032-67] Add docstrings

#### Implementation Tasks - Curl CFFI Middleware
- [ ] [TICKET-032-68] Create `scrapers/buxmax_scraper/middlewares/curl_cffi_middleware.py`
- [ ] [TICKET-032-69] Import curl_cffi modules
- [ ] [TICKET-032-70] Create `CurlCffiMiddleware` class
- [ ] [TICKET-032-71] Implement `process_request()` for TLS spoofing
- [ ] [TICKET-032-72] Configure browser impersonation (Chrome, Firefox)
- [ ] [TICKET-032-73] Handle SSL verification
- [ ] [TICKET-032-74] Add error handling for curl_cffi failures
- [ ] [TICKET-032-75] Add docstrings

#### Implementation Tasks - Enhanced Retry Logic
- [ ] [TICKET-032-76] Update `scrapers/buxmax_scraper/middlewares/retry_middleware.py`
- [ ] [TICKET-032-77] Add CAPTCHA detection logic
- [ ] [TICKET-032-78] Check for common CAPTCHA indicators in response
- [ ] [TICKET-032-79] Check for reCAPTCHA elements
- [ ] [TICKET-032-80] Check for hCaptcha elements
- [ ] [TICKET-032-81] Implement rate limiting detection
- [ ] [TICKET-032-82] Add exponential backoff for rate limits
- [ ] [TICKET-032-83] Implement temporary block detection
- [ ] [TICKET-032-84] Add longer delays for blocked sources
- [ ] [TICKET-032-85] Implement JavaScript error retry logic
- [ ] [TICKET-032-86] Log CAPTCHA encounters
- [ ] [TICKET-032-87] Update source status on CAPTCHA detection

#### Implementation Tasks - Source Model Updates
- [ ] [TICKET-032-88] Update `apps/aggregation/models.py` Source model
- [ ] [TICKET-032-89] Add `requires_javascript` field (BooleanField, default=False)
- [ ] [TICKET-032-90] Add `uses_anti_detection` field (BooleanField, default=False)
- [ ] [TICKET-032-91] Add `captcha_encountered_count` field (IntegerField, default=0)
- [ ] [TICKET-032-92] Add `last_captcha_at` field (DateTimeField, null=True)
- [ ] [TICKET-032-93] Add `blocked_status` field (CharField with choices)
- [ ] [TICKET-032-94] Add choices: 'active', 'rate_limited', 'captcha_blocked', 'ip_blocked'
- [ ] [TICKET-032-95] Add db_index=True to blocked_status

#### Implementation Tasks - User Agents and Proxies
- [ ] [TICKET-032-96] Create `scrapers/buxmax_scraper/user_agents.py`
- [ ] [TICKET-032-97] Add list of realistic Chrome user agents
- [ ] [TICKET-032-98] Add list of realistic Firefox user agents
- [ ] [TICKET-032-99] Add list of realistic Safari user agents
- [ ] [TICKET-032-100] Create function to get random user agent
- [ ] [TICKET-032-101] Create `scrapers/buxmax_scraper/proxies.py`
- [ ] [TICKET-032-102] Create ProxyRotator class
- [ ] [TICKET-032-103] Implement get_next_proxy() method
- [ ] [TICKET-032-104] Implement mark_proxy_failed() method
- [ ] [TICKET-032-105] Add proxy health tracking

#### Settings Tasks
- [ ] [TICKET-032-106] Update `config/settings/base.py`
- [ ] [TICKET-032-107] Add PLAYWRIGHT_ENABLED = True
- [ ] [TICKET-032-108] Add ANTI_DETECTION_ENABLED = True
- [ ] [TICKET-032-109] Add PROXY_POOL = [] (empty list, configure as needed)
- [ ] [TICKET-032-110] Add USER_AGENT_POOL = [] (will be loaded from user_agents.py)
- [ ] [TICKET-032-111] Add CAPTCHA_DETECTION_ENABLED = True
- [ ] [TICKET-032-112] Add JAVASCRIPT_RENDERING_TIMEOUT = 30000

#### Admin Tasks
- [ ] [TICKET-032-113] Update `apps/aggregation/admin.py` SourceAdmin
- [ ] [TICKET-032-114] Add requires_javascript to list_display
- [ ] [TICKET-032-115] Add blocked_status to list_display
- [ ] [TICKET-032-116] Add list_filter for requires_javascript
- [ ] [TICKET-032-117] Add list_filter for blocked_status
- [ ] [TICKET-032-118] Create `enable_javascript_rendering` admin action
- [ ] [TICKET-032-119] Create `enable_anti_detection` admin action
- [ ] [TICKET-032-120] Create `reset_block_status` admin action
- [ ] [TICKET-032-121] Create `test_scrape_with_playwright` admin action

#### Migration and Verification Tasks
- [ ] [TICKET-032-122] Run `python manage.py makemigrations aggregation`
- [ ] [TICKET-032-123] Run `python manage.py migrate`
- [ ] [TICKET-032-124] Run `python manage.py check`
- [ ] [TICKET-032-125] Run `scripts/install_playwright.sh`
- [ ] [TICKET-032-126] Verify Playwright browsers installed
- [ ] [TICKET-032-127] Create test Source requiring JavaScript
- [ ] [TICKET-032-128] Run JavaScriptBlogSpider manually
- [ ] [TICKET-032-129] Verify JavaScript content extracted
- [ ] [TICKET-032-130] Test infinite scroll handling
- [ ] [TICKET-032-131] Test "Load More" button clicking
- [ ] [TICKET-032-132] Verify user agent rotation working
- [ ] [TICKET-032-133] Verify request delays randomized
- [ ] [TICKET-032-134] Test CAPTCHA detection
- [ ] [TICKET-032-135] Verify source blocked_status updated
- [ ] [TICKET-032-136] Run `pytest scrapers/buxmax_scraper/tests/test_playwright_spider.py -v`
- [ ] [TICKET-032-137] Verify all tests pass

---

### TICKET-033: Enhanced Newsletter Distribution with ESP Integration
**Dependencies:** TICKET-017, TICKET-018

#### Test Tasks
- [ ] [TICKET-033-01] Create `apps/content/tests/test_esp_service.py` with imports
- [ ] [TICKET-033-02] Add `TestSendGridService` test class
- [ ] [TICKET-033-03] Write `test_send_email` test method (mocked SendGrid API)
- [ ] [TICKET-033-04] Write `test_send_bulk_emails` test method (mocked)
- [ ] [TICKET-033-05] Write `test_add_subscriber` test method (mocked)
- [ ] [TICKET-033-06] Add `TestMailchimpService` test class
- [ ] [TICKET-033-07] Write `test_send_email` test method (mocked Mailchimp API)
- [ ] [TICKET-033-08] Write `test_add_subscriber` test method (mocked)
- [ ] [TICKET-033-09] Add `TestWebhookViews` test class
- [ ] [TICKET-033-10] Write `test_sendgrid_webhook_processing` test method
- [ ] [TICKET-033-11] Write `test_mailchimp_webhook_processing` test method

#### Implementation Tasks - Dependencies
- [ ] [TICKET-033-12] Add `sendgrid>=6.10.0` to `requirements/base.txt`
- [ ] [TICKET-033-13] Add `mailchimp-marketing>=3.0.80` to `requirements/base.txt`
- [ ] [TICKET-033-14] Update `.env.example` with SENDGRID_API_KEY
- [ ] [TICKET-033-15] Update `.env.example` with SENDGRID_FROM_EMAIL
- [ ] [TICKET-033-16] Update `.env.example` with MAILCHIMP_API_KEY
- [ ] [TICKET-033-17] Update `.env.example` with MAILCHIMP_SERVER_PREFIX
- [ ] [TICKET-033-18] Update `.env.example` with MAILCHIMP_LIST_ID
- [ ] [TICKET-033-19] Update `.env.example` with ESP_PROVIDER

#### Implementation Tasks - Base ESP Service
- [ ] [TICKET-033-20] Create `apps/content/services/esp_service.py`
- [ ] [TICKET-033-21] Import ABC and abstractmethod
- [ ] [TICKET-033-22] Create `BaseESPService` abstract class
- [ ] [TICKET-033-23] Define abstract method `send_email(to_email, subject, html_content, text_content, from_email=None)`
- [ ] [TICKET-033-24] Define abstract method `send_bulk_emails(recipients, subject, html_content, text_content)`
- [ ] [TICKET-033-25] Define abstract method `add_subscriber(email, first_name='', last_name='', tags=[])`
- [ ] [TICKET-033-26] Define abstract method `remove_subscriber(email)`
- [ ] [TICKET-033-27] Define abstract method `update_subscriber(email, **kwargs)`
- [ ] [TICKET-033-28] Define abstract method `get_subscriber_status(email)`
- [ ] [TICKET-033-29] Define abstract method `track_email_event(event_type, email, newsletter_id, metadata={})`
- [ ] [TICKET-033-30] Add docstrings to base class and methods

#### Implementation Tasks - SendGrid Service
- [ ] [TICKET-033-31] Create `apps/content/services/sendgrid_service.py`
- [ ] [TICKET-033-32] Import sendgrid modules
- [ ] [TICKET-033-33] Create `SendGridService` class inheriting from BaseESPService
- [ ] [TICKET-033-34] Implement `__init__()` to initialize SendGrid client
- [ ] [TICKET-033-35] Load API key from settings
- [ ] [TICKET-033-36] Implement `send_email()` method
- [ ] [TICKET-033-37] Create Mail object with from/to/subject/content
- [ ] [TICKET-033-38] Send via SendGrid API
- [ ] [TICKET-033-39] Handle SendGrid exceptions
- [ ] [TICKET-033-40] Return success status and message_id
- [ ] [TICKET-033-41] Implement `send_bulk_emails()` method
- [ ] [TICKET-033-42] Batch recipients (max 1000 per batch)
- [ ] [TICKET-033-43] Create personalization for each recipient
- [ ] [TICKET-033-44] Send batches with delays
- [ ] [TICKET-033-45] Track sent count
- [ ] [TICKET-033-46] Implement `add_subscriber()` method
- [ ] [TICKET-033-47] Use Marketing Campaigns API
- [ ] [TICKET-033-48] Add contact to list
- [ ] [TICKET-033-49] Handle duplicate contacts
- [ ] [TICKET-033-50] Implement `remove_subscriber()` method
- [ ] [TICKET-033-51] Add to suppression list
- [ ] [TICKET-033-52] Implement `update_subscriber()` method
- [ ] [TICKET-033-53] Update contact fields
- [ ] [TICKET-033-54] Implement `get_subscriber_status()` method
- [ ] [TICKET-033-55] Query contact status
- [ ] [TICKET-033-56] Add retry logic with exponential backoff
- [ ] [TICKET-033-57] Add rate limit handling
- [ ] [TICKET-033-58] Add comprehensive logging
- [ ] [TICKET-033-59] Add docstrings to all methods

#### Implementation Tasks - Mailchimp Service
- [ ] [TICKET-033-60] Create `apps/content/services/mailchimp_service.py`
- [ ] [TICKET-033-61] Import mailchimp_marketing modules
- [ ] [TICKET-033-62] Create `MailchimpService` class inheriting from BaseESPService
- [ ] [TICKET-033-63] Implement `__init__()` to initialize Mailchimp client
- [ ] [TICKET-033-64] Load API key and server prefix from settings
- [ ] [TICKET-033-65] Implement `send_email()` method
- [ ] [TICKET-033-66] Use Transactional API (Mandrill)
- [ ] [TICKET-033-67] Create message object
- [ ] [TICKET-033-68] Send via Mailchimp API
- [ ] [TICKET-033-69] Handle Mailchimp exceptions
- [ ] [TICKET-033-70] Implement `send_bulk_emails()` method
- [ ] [TICKET-033-71] Create campaign
- [ ] [TICKET-033-72] Set campaign content
- [ ] [TICKET-033-73] Send campaign
- [ ] [TICKET-033-74] Implement `add_subscriber()` method
- [ ] [TICKET-033-75] Add member to list
- [ ] [TICKET-033-76] Set merge fields (first_name, last_name)
- [ ] [TICKET-033-77] Add tags
- [ ] [TICKET-033-78] Handle existing members
- [ ] [TICKET-033-79] Implement `remove_subscriber()` method
- [ ] [TICKET-033-80] Archive or delete member
- [ ] [TICKET-033-81] Implement `update_subscriber()` method
- [ ] [TICKET-033-82] Update member merge fields
- [ ] [TICKET-033-83] Update tags
- [ ] [TICKET-033-84] Implement `get_subscriber_status()` method
- [ ] [TICKET-033-85] Get member info
- [ ] [TICKET-033-86] Return subscription status
- [ ] [TICKET-033-87] Add error handling and logging
- [ ] [TICKET-033-88] Add docstrings to all methods

#### Implementation Tasks - ESP Factory
- [ ] [TICKET-033-89] Create `apps/content/services/esp_factory.py`
- [ ] [TICKET-033-90] Import SendGridService and MailchimpService
- [ ] [TICKET-033-91] Create `ESPFactory` class
- [ ] [TICKET-033-92] Add class variable for singleton instances
- [ ] [TICKET-033-93] Implement `get_esp_service()` class method
- [ ] [TICKET-033-94] Check ESP_PROVIDER setting
- [ ] [TICKET-033-95] Return SendGridService if provider is 'sendgrid'
- [ ] [TICKET-033-96] Return MailchimpService if provider is 'mailchimp'
- [ ] [TICKET-033-97] Return Django email backend if provider is 'django'
- [ ] [TICKET-033-98] Implement singleton pattern
- [ ] [TICKET-033-99] Add error handling for invalid provider
- [ ] [TICKET-033-100] Add docstrings

#### Implementation Tasks - Newsletter Model Updates
- [ ] [TICKET-033-101] Update `apps/content/models.py` Newsletter model
- [ ] [TICKET-033-102] Add `esp_campaign_id` field (CharField, null=True, blank=True)
- [ ] [TICKET-033-103] Add `esp_provider` field (CharField with choices)
- [ ] [TICKET-033-104] Add `sent_count` field (IntegerField, default=0)
- [ ] [TICKET-033-105] Add `delivered_count` field (IntegerField, default=0)
- [ ] [TICKET-033-106] Add `opened_count` field (IntegerField, default=0)
- [ ] [TICKET-033-107] Add `clicked_count` field (IntegerField, default=0)
- [ ] [TICKET-033-108] Add `bounced_count` field (IntegerField, default=0)
- [ ] [TICKET-033-109] Add `unsubscribed_count` field (IntegerField, default=0)
- [ ] [TICKET-033-110] Add `last_synced_at` field (DateTimeField, null=True)
- [ ] [TICKET-033-111] Implement `calculate_open_rate()` method
- [ ] [TICKET-033-112] Return percentage (opened / delivered * 100)
- [ ] [TICKET-033-113] Implement `calculate_click_rate()` method
- [ ] [TICKET-033-114] Return percentage (clicked / delivered * 100)
- [ ] [TICKET-033-115] Implement `sync_stats_from_esp()` method
- [ ] [TICKET-033-116] Call ESP API to fetch stats
- [ ] [TICKET-033-117] Update count fields
- [ ] [TICKET-033-118] Update last_synced_at

#### Implementation Tasks - EmailEvent Model
- [ ] [TICKET-033-119] Add `EmailEvent` model to `apps/content/models.py`
- [ ] [TICKET-033-120] Add `newsletter` field (ForeignKey to Newsletter)
- [ ] [TICKET-033-121] Add `subscriber` field (ForeignKey to EmailSubscriber)
- [ ] [TICKET-033-122] Add `event_type` field (CharField with choices)
- [ ] [TICKET-033-123] Add choices: 'sent', 'delivered', 'opened', 'clicked', 'bounced', 'unsubscribed', 'spam_report'
- [ ] [TICKET-033-124] Add `event_data` field (JSONField, default=dict)
- [ ] [TICKET-033-125] Add `esp_event_id` field (CharField, unique=True, db_index=True)
- [ ] [TICKET-033-126] Add `timestamp` field (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-033-127] Add `ip_address` field (GenericIPAddressField, null=True)
- [ ] [TICKET-033-128] Add `user_agent` field (TextField, blank=True)
- [ ] [TICKET-033-129] Add `url_clicked` field (URLField, null=True, blank=True)
- [ ] [TICKET-033-130] Add Meta class with indexes on (newsletter, event_type)
- [ ] [TICKET-033-131] Add index on (subscriber, event_type)
- [ ] [TICKET-033-132] Add `__str__()` method
- [ ] [TICKET-033-133] Add docstrings

#### Implementation Tasks - Update Newsletter Task
- [ ] [TICKET-033-134] Update `apps/content/tasks.py` send_newsletter task
- [ ] [TICKET-033-135] Import ESPFactory
- [ ] [TICKET-033-136] Get ESP service from factory
- [ ] [TICKET-033-137] Fetch active subscribers
- [ ] [TICKET-033-138] Batch subscribers (1000 per batch)
- [ ] [TICKET-033-139] Call esp_service.send_bulk_emails() for each batch
- [ ] [TICKET-033-140] Store esp_campaign_id in newsletter
- [ ] [TICKET-033-141] Update newsletter.sent_count
- [ ] [TICKET-033-142] Handle ESP-specific errors
- [ ] [TICKET-033-143] Log sending progress
- [ ] [TICKET-033-144] Update newsletter status to 'sent'

#### Implementation Tasks - Webhook Views
- [ ] [TICKET-033-145] Create `apps/content/views/webhook_views.py`
- [ ] [TICKET-033-146] Import necessary modules (json, hmac, hashlib)
- [ ] [TICKET-033-147] Import Django views (View, csrf_exempt)
- [ ] [TICKET-033-148] Create `SendGridWebhookView` class inheriting from View
- [ ] [TICKET-033-149] Add @csrf_exempt decorator
- [ ] [TICKET-033-150] Implement `post()` method
- [ ] [TICKET-033-151] Parse JSON payload from request body
- [ ] [TICKET-033-152] Verify webhook signature
- [ ] [TICKET-033-153] Loop through events in payload
- [ ] [TICKET-033-154] Extract event_type, email, timestamp
- [ ] [TICKET-033-155] Find corresponding Newsletter and EmailSubscriber
- [ ] [TICKET-033-156] Create EmailEvent record
- [ ] [TICKET-033-157] Update Newsletter statistics based on event_type
- [ ] [TICKET-033-158] Update EmailSubscriber status if bounced/unsubscribed
- [ ] [TICKET-033-159] Return HTTP 200 response
- [ ] [TICKET-033-160] Handle exceptions and return appropriate status codes
- [ ] [TICKET-033-161] Create `MailchimpWebhookView` class
- [ ] [TICKET-033-162] Add @csrf_exempt decorator
- [ ] [TICKET-033-163] Implement `post()` method
- [ ] [TICKET-033-164] Parse Mailchimp webhook payload
- [ ] [TICKET-033-165] Verify webhook signature
- [ ] [TICKET-033-166] Extract event data
- [ ] [TICKET-033-167] Create EmailEvent record
- [ ] [TICKET-033-168] Update statistics
- [ ] [TICKET-033-169] Return HTTP 200 response
- [ ] [TICKET-033-170] Add docstrings to views

#### Implementation Tasks - Stats Sync Task
- [ ] [TICKET-033-171] Update `apps/content/tasks.py` to add sync_newsletter_stats task
- [ ] [TICKET-033-172] Add @shared_task decorator
- [ ] [TICKET-033-173] Query newsletters sent in last 30 days
- [ ] [TICKET-033-174] Loop through newsletters
- [ ] [TICKET-033-175] Call newsletter.sync_stats_from_esp()
- [ ] [TICKET-033-176] Update delivered, opened, clicked counts
- [ ] [TICKET-033-177] Log sync results
- [ ] [TICKET-033-178] Handle ESP API errors
- [ ] [TICKET-033-179] Return sync summary
- [ ] [TICKET-033-180] Add to CELERY_BEAT_SCHEDULE (daily at 3 AM)

#### Implementation Tasks - Analytics Dashboard
- [ ] [TICKET-033-181] Create `apps/content/templates/content/newsletter_analytics.html`
- [ ] [TICKET-033-182] Extend base template
- [ ] [TICKET-033-183] Add page title "Newsletter Analytics"
- [ ] [TICKET-033-184] Create summary cards section
- [ ] [TICKET-033-185] Display total newsletters sent
- [ ] [TICKET-033-186] Display average open rate
- [ ] [TICKET-033-187] Display average click rate
- [ ] [TICKET-033-188] Display total subscribers
- [ ] [TICKET-033-189] Create newsletter list section
- [ ] [TICKET-033-190] Display table with newsletter details
- [ ] [TICKET-033-191] Show sent, delivered, opened, clicked counts
- [ ] [TICKET-033-192] Show open rate and click rate percentages
- [ ] [TICKET-033-193] Show bounce and unsubscribe counts
- [ ] [TICKET-033-194] Add Chart.js library
- [ ] [TICKET-033-195] Create open rate trend chart
- [ ] [TICKET-033-196] Create click rate trend chart
- [ ] [TICKET-033-197] Create event timeline section
- [ ] [TICKET-033-198] Display recent email events
- [ ] [TICKET-033-199] Add filters for event type and date range
- [ ] [TICKET-033-200] Create top clicked links section
- [ ] [TICKET-033-201] Query and display most clicked URLs
- [ ] [TICKET-033-202] Add CSS styling for dashboard

#### Implementation Tasks - Analytics View
- [ ] [TICKET-033-203] Create `apps/content/views/analytics_views.py`
- [ ] [TICKET-033-204] Import necessary modules
- [ ] [TICKET-033-205] Create `NewsletterAnalyticsView` class
- [ ] [TICKET-033-206] Inherit from PermissionRequiredMixin, TemplateView
- [ ] [TICKET-033-207] Set permission_required = 'content.view_newsletter'
- [ ] [TICKET-033-208] Set template_name = 'content/newsletter_analytics.html'
- [ ] [TICKET-033-209] Implement get_context_data()
- [ ] [TICKET-033-210] Query all newsletters with stats
- [ ] [TICKET-033-211] Calculate average open rate
- [ ] [TICKET-033-212] Calculate average click rate
- [ ] [TICKET-033-213] Get total subscriber count
- [ ] [TICKET-033-214] Get recent email events
- [ ] [TICKET-033-215] Get top clicked URLs
- [ ] [TICKET-033-216] Add all data to context
- [ ] [TICKET-033-217] Add docstrings

#### URL Configuration Tasks
- [ ] [TICKET-033-218] Update `apps/content/urls.py`
- [ ] [TICKET-033-219] Add webhook URL patterns
- [ ] [TICKET-033-220] Add path('webhooks/sendgrid/', SendGridWebhookView.as_view(), name='sendgrid_webhook')
- [ ] [TICKET-033-221] Add path('webhooks/mailchimp/', MailchimpWebhookView.as_view(), name='mailchimp_webhook')
- [ ] [TICKET-033-222] Add analytics URL pattern
- [ ] [TICKET-033-223] Add path('analytics/', NewsletterAnalyticsView.as_view(), name='newsletter_analytics')

#### Admin Tasks
- [ ] [TICKET-033-224] Update `apps/content/admin.py` NewsletterAdmin
- [ ] [TICKET-033-225] Add esp_campaign_id to readonly_fields
- [ ] [TICKET-033-226] Add sent_count to readonly_fields
- [ ] [TICKET-033-227] Add delivered_count to readonly_fields
- [ ] [TICKET-033-228] Add opened_count to readonly_fields
- [ ] [TICKET-033-229] Add clicked_count to readonly_fields
- [ ] [TICKET-033-230] Add bounced_count to readonly_fields
- [ ] [TICKET-033-231] Add unsubscribed_count to readonly_fields
- [ ] [TICKET-033-232] Add calculate_open_rate to list_display
- [ ] [TICKET-033-233] Add calculate_click_rate to list_display
- [ ] [TICKET-033-234] Create `sync_stats_from_esp` admin action
- [ ] [TICKET-033-235] Create `resend_to_failed` admin action
- [ ] [TICKET-033-236] Create `EmailEventAdmin` class
- [ ] [TICKET-033-237] Add list_display: newsletter, subscriber, event_type, timestamp
- [ ] [TICKET-033-238] Add list_filter: event_type, timestamp
- [ ] [TICKET-033-239] Add search_fields: subscriber__email
- [ ] [TICKET-033-240] Add readonly_fields for all fields
- [ ] [TICKET-033-241] Register EmailEvent with EmailEventAdmin

#### Settings Tasks
- [ ] [TICKET-033-242] Update `config/settings/base.py`
- [ ] [TICKET-033-243] Add ESP_PROVIDER = env('ESP_PROVIDER', default='django')
- [ ] [TICKET-033-244] Add SENDGRID_API_KEY = env('SENDGRID_API_KEY', default='')
- [ ] [TICKET-033-245] Add SENDGRID_FROM_EMAIL = env('SENDGRID_FROM_EMAIL', default='')
- [ ] [TICKET-033-246] Add MAILCHIMP_API_KEY = env('MAILCHIMP_API_KEY', default='')
- [ ] [TICKET-033-247] Add MAILCHIMP_SERVER_PREFIX = env('MAILCHIMP_SERVER_PREFIX', default='')
- [ ] [TICKET-033-248] Add MAILCHIMP_LIST_ID = env('MAILCHIMP_LIST_ID', default='')

#### Migration and Verification Tasks
- [ ] [TICKET-033-249] Run `python manage.py makemigrations content`
- [ ] [TICKET-033-250] Run `python manage.py migrate`
- [ ] [TICKET-033-251] Run `python manage.py check`
- [ ] [TICKET-033-252] Configure SendGrid API key in .env
- [ ] [TICKET-033-253] Test send_email() with SendGrid
- [ ] [TICKET-033-254] Verify email received
- [ ] [TICKET-033-255] Test send_bulk_emails() with batch
- [ ] [TICKET-033-256] Verify all emails sent
- [ ] [TICKET-033-257] Configure SendGrid webhook URL
- [ ] [TICKET-033-258] Send test email and trigger events
- [ ] [TICKET-033-259] Verify webhook receives events
- [ ] [TICKET-033-260] Verify EmailEvent records created
- [ ] [TICKET-033-261] Verify Newsletter statistics updated
- [ ] [TICKET-033-262] Test Mailchimp integration (if configured)
- [ ] [TICKET-033-263] Run sync_newsletter_stats task
- [ ] [TICKET-033-264] Verify stats synced from ESP
- [ ] [TICKET-033-265] Access newsletter analytics dashboard
- [ ] [TICKET-033-266] Verify charts display correctly
- [ ] [TICKET-033-267] Verify open/click rates calculated correctly
- [ ] [TICKET-033-268] Test admin actions (sync stats, resend)
- [ ] [TICKET-033-269] Run `pytest apps/content/tests/test_esp_service.py -v`
- [ ] [TICKET-033-270] Verify all tests pass

---

### TICKET-034: Advanced Monitoring - Scraper Health and AI Cost Tracking
**Dependencies:** TICKET-009, TICKET-014, TICKET-030

#### Test Tasks
- [ ] [TICKET-034-01] Create `apps/core/tests/test_monitoring_service.py` with imports
- [ ] [TICKET-034-02] Add `TestMonitoringService` test class
- [ ] [TICKET-034-03] Write `test_get_scraper_health_summary` test method
- [ ] [TICKET-034-04] Write `test_get_failing_sources` test method
- [ ] [TICKET-034-05] Write `test_get_ai_usage_summary` test method
- [ ] [TICKET-034-06] Write `test_calculate_daily_ai_cost` test method
- [ ] [TICKET-034-07] Write `test_get_system_health_score` test method
- [ ] [TICKET-034-08] Add `TestAlertingService` test class
- [ ] [TICKET-034-09] Write `test_check_scraper_health` test method (mocked alerts)
- [ ] [TICKET-034-10] Write `test_check_ai_cost_budget` test method (mocked alerts)

#### Implementation Tasks - ScraperHealthLog Model
- [ ] [TICKET-034-11] Update `apps/aggregation/models.py` to add ScraperHealthLog model
- [ ] [TICKET-034-12] Add `source` field (ForeignKey to Source)
- [ ] [TICKET-034-13] Add `spider_name` field (CharField, max_length=100, db_index=True)
- [ ] [TICKET-034-14] Add `run_timestamp` field (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-034-15] Add `status` field (CharField with choices, db_index=True)
- [ ] [TICKET-034-16] Add choices: 'success', 'partial_success', 'failed', 'blocked', 'captcha'
- [ ] [TICKET-034-17] Add `items_scraped` field (IntegerField, default=0)
- [ ] [TICKET-034-18] Add `items_failed` field (IntegerField, default=0)
- [ ] [TICKET-034-19] Add `duration_seconds` field (FloatField)
- [ ] [TICKET-034-20] Add `error_type` field (CharField, null=True, blank=True)
- [ ] [TICKET-034-21] Add `error_message` field (TextField, blank=True)
- [ ] [TICKET-034-22] Add `http_status_codes` field (JSONField, default=dict)
- [ ] [TICKET-034-23] Add `retry_count` field (IntegerField, default=0)
- [ ] [TICKET-034-24] Add `memory_usage_mb` field (FloatField, null=True)
- [ ] [TICKET-034-25] Add `cpu_usage_percent` field (FloatField, null=True)
- [ ] [TICKET-034-26] Implement `is_healthy()` method
- [ ] [TICKET-034-27] Return boolean based on status and error rate
- [ ] [TICKET-034-28] Implement `calculate_success_rate()` method
- [ ] [TICKET-034-29] Return percentage of successful items
- [ ] [TICKET-034-30] Add `__str__()` method
- [ ] [TICKET-034-31] Add Meta class with db_table and indexes
- [ ] [TICKET-034-32] Add docstrings

#### Implementation Tasks - AIUsageLog Model
- [ ] [TICKET-034-33] Update `apps/content/models.py` to add AIUsageLog model
- [ ] [TICKET-034-34] Add `timestamp` field (DateTimeField, auto_now_add=True, db_index=True)
- [ ] [TICKET-034-35] Add `provider` field (CharField with choices, db_index=True)
- [ ] [TICKET-034-36] Add choices: 'openai', 'anthropic'
- [ ] [TICKET-034-37] Add `model` field (CharField, max_length=100, db_index=True)
- [ ] [TICKET-034-38] Add `task_type` field (CharField with choices, db_index=True)
- [ ] [TICKET-034-39] Add choices: 'article_generation', 'summary', 'moderation', 'avatar_response'
- [ ] [TICKET-034-40] Add `prompt_tokens` field (IntegerField)
- [ ] [TICKET-034-41] Add `completion_tokens` field (IntegerField)
- [ ] [TICKET-034-42] Add `total_tokens` field (IntegerField)
- [ ] [TICKET-034-43] Add `estimated_cost_usd` field (DecimalField, max_digits=10, decimal_places=6)
- [ ] [TICKET-034-44] Add `latency_ms` field (IntegerField)
- [ ] [TICKET-034-45] Add `success` field (BooleanField, default=True, db_index=True)
- [ ] [TICKET-034-46] Add `error_message` field (TextField, blank=True)
- [ ] [TICKET-034-47] Add `related_object_type` field (CharField, null=True)
- [ ] [TICKET-034-48] Add `related_object_id` field (IntegerField, null=True)
- [ ] [TICKET-034-49] Implement `calculate_cost()` method
- [ ] [TICKET-034-50] Calculate based on provider pricing
- [ ] [TICKET-034-51] OpenAI: GPT-4o pricing
- [ ] [TICKET-034-52] Anthropic: Claude pricing
- [ ] [TICKET-034-53] Add `__str__()` method
- [ ] [TICKET-034-54] Add Meta class with indexes on (timestamp, provider), (task_type, timestamp)
- [ ] [TICKET-034-55] Add docstrings

#### Implementation Tasks - Update Scraping Tasks
- [ ] [TICKET-034-56] Update `apps/aggregation/tasks.py` scraping tasks
- [ ] [TICKET-034-57] Import time, psutil for tracking
- [ ] [TICKET-034-58] Track start_time at task beginning
- [ ] [TICKET-034-59] Track items_scraped count
- [ ] [TICKET-034-60] Track items_failed count
- [ ] [TICKET-034-61] Capture HTTP status codes encountered
- [ ] [TICKET-034-62] Measure memory usage with psutil
- [ ] [TICKET-034-63] Measure CPU usage with psutil
- [ ] [TICKET-034-64] Calculate duration_seconds
- [ ] [TICKET-034-65] Determine status based on results
- [ ] [TICKET-034-66] Create ScraperHealthLog entry
- [ ] [TICKET-034-67] Handle exceptions and log error details
- [ ] [TICKET-034-68] Store error_type and error_message

#### Implementation Tasks - Update AI Service
- [ ] [TICKET-034-69] Update `apps/content/services/ai_service.py`
- [ ] [TICKET-034-70] Import time for latency tracking
- [ ] [TICKET-034-71] Track start_time before API call
- [ ] [TICKET-034-72] Extract token counts from API response
- [ ] [TICKET-034-73] Calculate latency_ms
- [ ] [TICKET-034-74] Determine provider and model
- [ ] [TICKET-034-75] Calculate estimated_cost_usd
- [ ] [TICKET-034-76] Create AIUsageLog entry
- [ ] [TICKET-034-77] Store task_type from context
- [ ] [TICKET-034-78] Store related_object_type and related_object_id
- [ ] [TICKET-034-79] Handle API errors and log failures
- [ ] [TICKET-034-80] Set success=False on error

#### Implementation Tasks - Monitoring Service
- [ ] [TICKET-034-81] Create `apps/core/services/monitoring_service.py`
- [ ] [TICKET-034-82] Import necessary modules (datetime, timedelta, etc.)
- [ ] [TICKET-034-83] Create `MonitoringService` class
- [ ] [TICKET-034-84] Implement `get_scraper_health_summary(days=7)` method
- [ ] [TICKET-034-85] Query ScraperHealthLog for last N days
- [ ] [TICKET-034-86] Aggregate success/failure counts
- [ ] [TICKET-034-87] Calculate average duration
- [ ] [TICKET-034-88] Return summary dictionary
- [ ] [TICKET-034-89] Implement `get_failing_sources(threshold=0.5)` method
- [ ] [TICKET-034-90] Query sources with low success rate
- [ ] [TICKET-034-91] Calculate success rate per source
- [ ] [TICKET-034-92] Filter by threshold
- [ ] [TICKET-034-93] Return list of failing sources
- [ ] [TICKET-034-94] Implement `get_blocked_sources()` method
- [ ] [TICKET-034-95] Query sources with blocked/captcha status
- [ ] [TICKET-034-96] Return list with last block time
- [ ] [TICKET-034-97] Implement `get_ai_usage_summary(days=30)` method
- [ ] [TICKET-034-98] Query AIUsageLog for last N days
- [ ] [TICKET-034-99] Aggregate total tokens
- [ ] [TICKET-034-100] Sum total costs
- [ ] [TICKET-034-101] Calculate average latency
- [ ] [TICKET-034-102] Return summary dictionary
- [ ] [TICKET-034-103] Implement `get_ai_cost_by_task_type(days=30)` method
- [ ] [TICKET-034-104] Group by task_type
- [ ] [TICKET-034-105] Sum costs per task type
- [ ] [TICKET-034-106] Return breakdown dictionary
- [ ] [TICKET-034-107] Implement `get_ai_cost_by_provider(days=30)` method
- [ ] [TICKET-034-108] Group by provider
- [ ] [TICKET-034-109] Sum costs per provider
- [ ] [TICKET-034-110] Return breakdown dictionary
- [ ] [TICKET-034-111] Implement `calculate_daily_ai_cost()` method
- [ ] [TICKET-034-112] Query today's AIUsageLog entries
- [ ] [TICKET-034-113] Sum estimated_cost_usd
- [ ] [TICKET-034-114] Return total cost
- [ ] [TICKET-034-115] Implement `calculate_monthly_ai_cost()` method
- [ ] [TICKET-034-116] Query current month's entries
- [ ] [TICKET-034-117] Sum costs
- [ ] [TICKET-034-118] Return total
- [ ] [TICKET-034-119] Implement `predict_monthly_ai_cost()` method
- [ ] [TICKET-034-120] Calculate daily average
- [ ] [TICKET-034-121] Project to end of month
- [ ] [TICKET-034-122] Return projection
- [ ] [TICKET-034-123] Implement `get_system_health_score()` method
- [ ] [TICKET-034-124] Check scraper health (weight: 30%)
- [ ] [TICKET-034-125] Check AI success rate (weight: 20%)
- [ ] [TICKET-034-126] Check Celery queue lengths (weight: 25%)
- [ ] [TICKET-034-127] Check database performance (weight: 15%)
- [ ] [TICKET-034-128] Check Redis cache hit rate (weight: 10%)
- [ ] [TICKET-034-129] Calculate weighted score (0-100)
- [ ] [TICKET-034-130] Return score and component details
- [ ] [TICKET-034-131] Add docstrings to all methods

#### Implementation Tasks - Alerting Service
- [ ] [TICKET-034-132] Create `apps/core/services/alerting_service.py`
- [ ] [TICKET-034-133] Import necessary modules (smtplib, requests for Slack)
- [ ] [TICKET-034-134] Create `AlertingService` class
- [ ] [TICKET-034-135] Implement `check_scraper_health()` method
- [ ] [TICKET-034-136] Get failing sources from MonitoringService
- [ ] [TICKET-034-137] Check if failure rate exceeds threshold
- [ ] [TICKET-034-138] Call send_alert() if threshold exceeded
- [ ] [TICKET-034-139] Implement `check_ai_cost_budget()` method
- [ ] [TICKET-034-140] Get daily cost from MonitoringService
- [ ] [TICKET-034-141] Compare to AI_DAILY_BUDGET_USD setting
- [ ] [TICKET-034-142] Call send_alert() if budget exceeded
- [ ] [TICKET-034-143] Get monthly cost projection
- [ ] [TICKET-034-144] Compare to AI_MONTHLY_BUDGET_USD
- [ ] [TICKET-034-145] Alert if projection exceeds budget
- [ ] [TICKET-034-146] Implement `check_celery_queues()` method
- [ ] [TICKET-034-147] Inspect Celery queue lengths
- [ ] [TICKET-034-148] Alert if queues backing up (>1000 tasks)
- [ ] [TICKET-034-149] Implement `check_error_rates()` method
- [ ] [TICKET-034-150] Query recent error logs
- [ ] [TICKET-034-151] Calculate error rate
- [ ] [TICKET-034-152] Alert if rate spikes above threshold
- [ ] [TICKET-034-153] Implement `send_alert(alert_type, message, severity)` method
- [ ] [TICKET-034-154] Format alert message
- [ ] [TICKET-034-155] Send email to ALERT_EMAIL_RECIPIENTS
- [ ] [TICKET-034-156] Send to Slack webhook if configured
- [ ] [TICKET-034-157] Log alert sent
- [ ] [TICKET-034-158] Add docstrings to all methods

#### Implementation Tasks - Dashboard Views
- [ ] [TICKET-034-159] Create `apps/core/views/monitoring_views.py`
- [ ] [TICKET-034-160] Import necessary modules
- [ ] [TICKET-034-161] Create `ScraperHealthDashboardView` class
- [ ] [TICKET-034-162] Inherit from PermissionRequiredMixin, TemplateView
- [ ] [TICKET-034-163] Set permission_required = 'core.view_monitoring'
- [ ] [TICKET-034-164] Set template_name = 'monitoring/scraper_health.html'
- [ ] [TICKET-034-165] Implement get_context_data()
- [ ] [TICKET-034-166] Get scraper health summary from MonitoringService
- [ ] [TICKET-034-167] Get failing sources
- [ ] [TICKET-034-168] Get blocked sources
- [ ] [TICKET-034-169] Get scraping volume trends (last 30 days)
- [ ] [TICKET-034-170] Add all data to context
- [ ] [TICKET-034-171] Create `AIUsageDashboardView` class
- [ ] [TICKET-034-172] Set template_name = 'monitoring/ai_usage.html'
- [ ] [TICKET-034-173] Implement get_context_data()
- [ ] [TICKET-034-174] Get AI usage summary
- [ ] [TICKET-034-175] Get cost breakdown by task type
- [ ] [TICKET-034-176] Get cost breakdown by provider
- [ ] [TICKET-034-177] Get daily and monthly costs
- [ ] [TICKET-034-178] Get cost projection
- [ ] [TICKET-034-179] Calculate budget utilization percentage
- [ ] [TICKET-034-180] Add all data to context
- [ ] [TICKET-034-181] Create `SystemHealthDashboardView` class
- [ ] [TICKET-034-182] Set template_name = 'monitoring/system_health.html'
- [ ] [TICKET-034-183] Implement get_context_data()
- [ ] [TICKET-034-184] Get system health score
- [ ] [TICKET-034-185] Get Celery queue lengths
- [ ] [TICKET-034-186] Get database performance metrics
- [ ] [TICKET-034-187] Get Redis cache hit rates
- [ ] [TICKET-034-188] Get recent errors summary
- [ ] [TICKET-034-189] Add all data to context
- [ ] [TICKET-034-190] Add docstrings to all views

#### Implementation Tasks - Dashboard Templates
- [ ] [TICKET-034-191] Create `apps/core/templates/monitoring/scraper_health.html`
- [ ] [TICKET-034-192] Extend base template
- [ ] [TICKET-034-193] Add page title "Scraper Health Dashboard"
- [ ] [TICKET-034-194] Create summary cards section
- [ ] [TICKET-034-195] Display total sources, active sources, failing sources
- [ ] [TICKET-034-196] Display average success rate
- [ ] [TICKET-034-197] Create success rate chart (Chart.js)
- [ ] [TICKET-034-198] Plot success rate over time (last 30 days)
- [ ] [TICKET-034-199] Create items scraped chart
- [ ] [TICKET-034-200] Plot daily scraping volume
- [ ] [TICKET-034-201] Create failing sources table
- [ ] [TICKET-034-202] Display source name, failure rate, last error
- [ ] [TICKET-034-203] Add action buttons (retry, disable)
- [ ] [TICKET-034-204] Create blocked sources table
- [ ] [TICKET-034-205] Display source name, block type, last block time
- [ ] [TICKET-034-206] Add CSS styling
- [ ] [TICKET-034-207] Create `apps/core/templates/monitoring/ai_usage.html`
- [ ] [TICKET-034-208] Extend base template
- [ ] [TICKET-034-209] Add page title "AI Usage & Cost Dashboard"
- [ ] [TICKET-034-210] Create cost summary cards
- [ ] [TICKET-034-211] Display daily cost, monthly cost, projected cost
- [ ] [TICKET-034-212] Display budget utilization percentage
- [ ] [TICKET-034-213] Create daily cost trend chart
- [ ] [TICKET-034-214] Plot cost over last 30 days
- [ ] [TICKET-034-215] Create cost by task type pie chart
- [ ] [TICKET-034-216] Show breakdown of costs
- [ ] [TICKET-034-217] Create cost by provider bar chart
- [ ] [TICKET-034-218] Compare OpenAI vs Anthropic costs
- [ ] [TICKET-034-219] Create token usage metrics section
- [ ] [TICKET-034-220] Display total tokens, average latency
- [ ] [TICKET-034-221] Create budget alert indicator
- [ ] [TICKET-034-222] Show warning if approaching budget
- [ ] [TICKET-034-223] Add CSS styling
- [ ] [TICKET-034-224] Create `apps/core/templates/monitoring/system_health.html`
- [ ] [TICKET-034-225] Extend base template
- [ ] [TICKET-034-226] Add page title "System Health Dashboard"
- [ ] [TICKET-034-227] Create health score gauge
- [ ] [TICKET-034-228] Display overall score (0-100) with color coding
- [ ] [TICKET-034-229] Create service status section
- [ ] [TICKET-034-230] Display database status indicator
- [ ] [TICKET-034-231] Display Redis status indicator
- [ ] [TICKET-034-232] Display Celery worker status
- [ ] [TICKET-034-233] Create Celery queue metrics
- [ ] [TICKET-034-234] Display queue lengths for each queue
- [ ] [TICKET-034-235] Create recent errors section
- [ ] [TICKET-034-236] Display last 10 errors with timestamps
- [ ] [TICKET-034-237] Create performance metrics section
- [ ] [TICKET-034-238] Display database query times
- [ ] [TICKET-034-239] Display cache hit rates
- [ ] [TICKET-034-240] Add CSS styling

#### Implementation Tasks - Monitoring Tasks
- [ ] [TICKET-034-241] Update `apps/core/tasks.py` to add monitoring tasks
- [ ] [TICKET-034-242] Create `check_system_health()` task with @shared_task
- [ ] [TICKET-034-243] Instantiate AlertingService
- [ ] [TICKET-034-244] Call check_scraper_health()
- [ ] [TICKET-034-245] Call check_ai_cost_budget()
- [ ] [TICKET-034-246] Call check_celery_queues()
- [ ] [TICKET-034-247] Call check_error_rates()
- [ ] [TICKET-034-248] Log health check results
- [ ] [TICKET-034-249] Create `cleanup_old_logs(days=90)` task
- [ ] [TICKET-034-250] Delete ScraperHealthLog older than N days
- [ ] [TICKET-034-251] Delete AIUsageLog older than N days
- [ ] [TICKET-034-252] Log cleanup results
- [ ] [TICKET-034-253] Create `generate_daily_report()` task
- [ ] [TICKET-034-254] Get scraper health summary
- [ ] [TICKET-034-255] Get AI usage summary
- [ ] [TICKET-034-256] Get system health score
- [ ] [TICKET-034-257] Format report email
- [ ] [TICKET-034-258] Send to ALERT_EMAIL_RECIPIENTS
- [ ] [TICKET-034-259] Create `generate_weekly_report()` task
- [ ] [TICKET-034-260] Get weekly statistics
- [ ] [TICKET-034-261] Format comprehensive report
- [ ] [TICKET-034-262] Send email
- [ ] [TICKET-034-263] Add docstrings to all tasks

#### Celery Beat Schedule Tasks
- [ ] [TICKET-034-264] Update CELERY_BEAT_SCHEDULE in `config/settings/base.py`
- [ ] [TICKET-034-265] Add 'check-system-health' task (every 15 minutes)
- [ ] [TICKET-034-266] Add 'cleanup-old-logs' task (daily at 2 AM)
- [ ] [TICKET-034-267] Add 'generate-daily-report' task (daily at 8 AM)
- [ ] [TICKET-034-268] Add 'generate-weekly-report' task (Monday at 9 AM)

#### Implementation Tasks - Management Commands
- [ ] [TICKET-034-269] Create `apps/core/management/commands/scraper_health_report.py`
- [ ] [TICKET-034-270] Create Command class
- [ ] [TICKET-034-271] Implement handle() method
- [ ] [TICKET-034-272] Get scraper health summary from MonitoringService
- [ ] [TICKET-034-273] Display summary in terminal with formatting
- [ ] [TICKET-034-274] Display failing sources table
- [ ] [TICKET-034-275] Display blocked sources table
- [ ] [TICKET-034-276] Add color coding (green/yellow/red)
- [ ] [TICKET-034-277] Create `apps/core/management/commands/ai_cost_report.py`
- [ ] [TICKET-034-278] Create Command class
- [ ] [TICKET-034-279] Implement handle() method
- [ ] [TICKET-034-280] Get AI usage summary
- [ ] [TICKET-034-281] Display daily and monthly costs
- [ ] [TICKET-034-282] Display breakdown by task type
- [ ] [TICKET-034-283] Display breakdown by provider
- [ ] [TICKET-034-284] Display cost projection
- [ ] [TICKET-034-285] Add budget utilization indicator
- [ ] [TICKET-034-286] Add color coding

#### Implementation Tasks - API Endpoints
- [ ] [TICKET-034-287] Create `apps/core/api/monitoring_api.py`
- [ ] [TICKET-034-288] Import DRF modules (APIView, Response)
- [ ] [TICKET-034-289] Create `ScraperHealthAPIView` class
- [ ] [TICKET-034-290] Add authentication requirement
- [ ] [TICKET-034-291] Implement get() method
- [ ] [TICKET-034-292] Get scraper health data from MonitoringService
- [ ] [TICKET-034-293] Return JSON response
- [ ] [TICKET-034-294] Create `AIUsageAPIView` class
- [ ] [TICKET-034-295] Implement get() method
- [ ] [TICKET-034-296] Get AI usage data
- [ ] [TICKET-034-297] Return JSON response
- [ ] [TICKET-034-298] Create `SystemHealthAPIView` class
- [ ] [TICKET-034-299] Implement get() method
- [ ] [TICKET-034-300] Get system health data
- [ ] [TICKET-034-301] Return JSON response
- [ ] [TICKET-034-302] Add docstrings to all views

#### URL Configuration Tasks
- [ ] [TICKET-034-303] Update `apps/core/urls.py` to add monitoring URLs
- [ ] [TICKET-034-304] Add path('monitoring/scraper-health/', ScraperHealthDashboardView.as_view())
- [ ] [TICKET-034-305] Add path('monitoring/ai-usage/', AIUsageDashboardView.as_view())
- [ ] [TICKET-034-306] Add path('monitoring/system-health/', SystemHealthDashboardView.as_view())
- [ ] [TICKET-034-307] Update `config/urls.py` to include monitoring API URLs
- [ ] [TICKET-034-308] Add path('api/monitoring/scraper-health/', ScraperHealthAPIView.as_view())
- [ ] [TICKET-034-309] Add path('api/monitoring/ai-usage/', AIUsageAPIView.as_view())
- [ ] [TICKET-034-310] Add path('api/monitoring/system-health/', SystemHealthAPIView.as_view())

#### Settings Tasks
- [ ] [TICKET-034-311] Update `config/settings/base.py` to add monitoring settings
- [ ] [TICKET-034-312] Add MONITORING_ENABLED = True
- [ ] [TICKET-034-313] Add ALERT_EMAIL_RECIPIENTS = env.list('ALERT_EMAIL_RECIPIENTS', default=[])
- [ ] [TICKET-034-314] Add SLACK_WEBHOOK_URL = env('SLACK_WEBHOOK_URL', default=None)
- [ ] [TICKET-034-315] Add AI_MONTHLY_BUDGET_USD = env.float('AI_MONTHLY_BUDGET_USD', default=500.0)
- [ ] [TICKET-034-316] Add AI_DAILY_BUDGET_USD = env.float('AI_DAILY_BUDGET_USD', default=20.0)
- [ ] [TICKET-034-317] Add SCRAPER_FAILURE_THRESHOLD = 0.5
- [ ] [TICKET-034-318] Add HEALTH_LOG_RETENTION_DAYS = 90
- [ ] [TICKET-034-319] Update `.env.example` with monitoring variables

#### Admin Tasks
- [ ] [TICKET-034-320] Update `apps/aggregation/admin.py` to add ScraperHealthLogAdmin
- [ ] [TICKET-034-321] Add list_display: source, spider_name, status, items_scraped, duration_seconds, run_timestamp
- [ ] [TICKET-034-322] Add list_filter: status, spider_name, run_timestamp
- [ ] [TICKET-034-323] Add search_fields: source__name, error_message
- [ ] [TICKET-034-324] Add readonly_fields for all fields
- [ ] [TICKET-034-325] Register ScraperHealthLog with ScraperHealthLogAdmin
- [ ] [TICKET-034-326] Update `apps/content/admin.py` to add AIUsageLogAdmin
- [ ] [TICKET-034-327] Add list_display: timestamp, provider, model, task_type, total_tokens, estimated_cost_usd
- [ ] [TICKET-034-328] Add list_filter: provider, model, task_type, success, timestamp
- [ ] [TICKET-034-329] Add search_fields: error_message
- [ ] [TICKET-034-330] Add readonly_fields for all fields
- [ ] [TICKET-034-331] Add custom changelist view to show total cost
- [ ] [TICKET-034-332] Register AIUsageLog with AIUsageLogAdmin

#### Migration and Verification Tasks
- [ ] [TICKET-034-333] Run `python manage.py makemigrations aggregation`
- [ ] [TICKET-034-334] Run `python manage.py makemigrations content`
- [ ] [TICKET-034-335] Run `python manage.py migrate`
- [ ] [TICKET-034-336] Run `python manage.py check`
- [ ] [TICKET-034-337] Run a scraping task
- [ ] [TICKET-034-338] Verify ScraperHealthLog entry created
- [ ] [TICKET-034-339] Check log has correct status, duration, items_scraped
- [ ] [TICKET-034-340] Run an AI generation task
- [ ] [TICKET-034-341] Verify AIUsageLog entry created
- [ ] [TICKET-034-342] Check log has correct tokens, cost, latency
- [ ] [TICKET-034-343] Access scraper health dashboard
- [ ] [TICKET-034-344] Verify charts display correctly
- [ ] [TICKET-034-345] Verify failing sources table shows data
- [ ] [TICKET-034-346] Access AI usage dashboard
- [ ] [TICKET-034-347] Verify cost metrics display correctly
- [ ] [TICKET-034-348] Verify budget utilization shown
- [ ] [TICKET-034-349] Access system health dashboard
- [ ] [TICKET-034-350] Verify health score calculated
- [ ] [TICKET-034-351] Verify service status indicators work
- [ ] [TICKET-034-352] Run check_system_health task manually
- [ ] [TICKET-034-353] Verify alerts sent if thresholds exceeded
- [ ] [TICKET-034-354] Run cleanup_old_logs task
- [ ] [TICKET-034-355] Verify old logs deleted
- [ ] [TICKET-034-356] Run generate_daily_report task
- [ ] [TICKET-034-357] Verify email report received
- [ ] [TICKET-034-358] Run `python manage.py scraper_health_report`
- [ ] [TICKET-034-359] Verify CLI report displays correctly
- [ ] [TICKET-034-360] Run `python manage.py ai_cost_report`
- [ ] [TICKET-034-361] Verify CLI cost report displays
- [ ] [TICKET-034-362] Test API endpoints with authentication
- [ ] [TICKET-034-363] Verify JSON responses correct
- [ ] [TICKET-034-364] Run `pytest apps/core/tests/test_monitoring_service.py -v`
- [ ] [TICKET-034-365] Verify all tests pass

---

## Checklist Complete!

**Total Tickets:** 34
**Total Atomic Tasks:** ~4,100+

**Summary by Phase:**
- **Phase 1 (Tickets 1-13):** Core Infrastructure & Aggregation MVP - ~850 tasks
- **Phase 2 (Tickets 14-18):** AI Content Generation & Distribution - ~650 tasks
- **Phase 3 (Tickets 19-23):** Community Forum MVP - ~750 tasks
- **Phase 4 (Tickets 24-30):** AI Avatars & Moderation - ~850 tasks
- **Phase 5 (Tickets 31-34):** Advanced Features - ~1,000 tasks

**Phase 5 Advanced Features Breakdown:**
- **TICKET-031 (123 tasks):** Automated source discovery with AI vetting
- **TICKET-032 (137 tasks):** JavaScript rendering and anti-detection
- **TICKET-033 (270 tasks):** ESP integration with webhook tracking
- **TICKET-034 (365 tasks):** Advanced monitoring dashboards

**Usage Instructions:**
1. Work through tickets sequentially, respecting dependencies
2. Check off each task as completed: `[ ]` → `[x]`
3. Run verification tasks after each ticket
4. Follow TDD: Tests → Implementation → Verification
5. Commit after each ticket with descriptive message
6. Never skip test tasks

**Progress Tracking:**
Update this checklist in git after completing each ticket to maintain progress visibility.

**Phase 5 Notes:**
- Phase 5 tickets are optional but highly recommended for production
- Can be implemented after Phase 4 is complete and stable
- Each ticket adds significant operational capabilities
- Total estimated time for Phase 5: 8-12 weeks

**Total Development Timeline:**
- Phase 1: 4-6 weeks
- Phase 2: 4-6 weeks
- Phase 3: 5-7 weeks
- Phase 4: 6-8 weeks
- Phase 5: 8-12 weeks
- **Total: 27-39 weeks (6-9 months)**

**Total Tickets:** 34
**Total Atomic Tasks:** ~3,600+

**Summary by Phase:**
- **Phase 1 (Tickets 1-13):** Core Infrastructure & Aggregation MVP - ~850 tasks
- **Phase 2 (Tickets 14-18):** AI Content Generation & Distribution - ~650 tasks
- **Phase 3 (Tickets 19-23):** Community Forum MVP - ~750 tasks
- **Phase 4 (Tickets 24-30):** AI Avatars & Moderation - ~850 tasks
- **Phase 5 (Tickets 31-34):** Advanced Features - ~500 tasks

**Phase 5 Advanced Features:**
- **TICKET-031 (123 tasks):** Automated source discovery with AI vetting
- **TICKET-032 (~120 tasks):** JavaScript rendering and anti-detection
- **TICKET-033 (~130 tasks):** ESP integration with webhook tracking
- **TICKET-034 (~130 tasks):** Advanced monitoring dashboards

**Usage Instructions:**
1. Work through tickets sequentially, respecting dependencies
2. Check off each task as completed: `[ ]` → `[x]`
3. Run verification tasks after each ticket
4. Follow TDD: Tests → Implementation → Verification
5. Commit after each ticket with descriptive message
6. Never skip test tasks

**Progress Tracking:**
Update this checklist in git after completing each ticket to maintain progress visibility.

**Note:** Tickets 32-34 follow the same granular task breakdown pattern as TICKET-031. Each ticket includes:
- Test tasks (10-15 tasks)
- Implementation tasks broken down by component (60-90 tasks)
- Configuration and admin tasks (10-15 tasks)
- Migration and verification tasks (10-15 tasks)

