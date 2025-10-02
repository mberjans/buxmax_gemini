# Buxmax Gemini - Development Tickets

## Overview

This document contains detailed software development tickets for implementing the Frugal Living Content Aggregation and Generation Platform. Each ticket is designed to be independently implementable by an AI coding agent or human developer.

**Total Tickets**: 130
**Organized by**: 10 Implementation Phases
**Reference Document**: `docs/enhanced_plan.md`

---

# Phase 1: Foundation Setup (BUXMAX-001 to BUXMAX-010)

## BUXMAX-001: Initialize Django Project Structure

**Type**: Setup
**Priority**: Critical  
**Complexity**: Small (1-2 hours)
**Dependencies**: None

### Description
Create the base Django project structure with the recommended directory layout, including all necessary configuration directories and placeholder files.

### Acceptance Criteria
- [ ] Django project created with name `buxmax_gemini`
- [ ] Directory structure matches enhanced_plan.md Section 14.1
- [ ] All required directories created (config, apps, scrapers, static, templates, logs, scripts)
- [ ] Empty `__init__.py` files in all Python packages
- [ ] `.gitignore` file created with appropriate patterns
- [ ] `README.md` created with project description

### Implementation Details
- Reference: enhanced_plan.md Section 14.1 (lines 649-891)
- Files to create:
  - `manage.py`
  - `config/__init__.py`
  - `config/settings/__init__.py`
  - `config/urls.py`
  - `config/wsgi.py`
  - `config/asgi.py`
  - `apps/__init__.py`
  - `.gitignore`
  - `README.md`
- Commands to run:
  ```bash
  django-admin startproject config .
  mkdir -p config/settings apps scrapers static templates logs scripts media
  ```

### Testing Requirements
- Verify project structure: `tree -L 3` (or `ls -R`)
- Run Django check: `python manage.py check`
- Expected output: "System check identified no issues (0 silenced)."

---

## BUXMAX-002: Create Requirements Files

**Type**: Configuration
**Priority**: Critical  
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-001

### Description
Create three requirements files (base, development, production) with all necessary dependencies and pinned versions as specified in the enhanced plan.

### Acceptance Criteria
- [ ] `requirements/` directory created
- [ ] `requirements/base.txt` created with 30+ core dependencies
- [ ] `requirements/development.txt` created with testing/debugging tools
- [ ] `requirements/production.txt` created with production dependencies
- [ ] All versions pinned to specific releases
- [ ] Dependencies organized by category with comments

### Implementation Details
- Reference: enhanced_plan.md Section 15.2 (lines 4011-4100)
- Files to create:
  - `requirements/base.txt`
  - `requirements/development.txt`
  - `requirements/production.txt`
- Key dependencies:
  - Django==4.2.11
  - celery[redis]==5.3.6
  - scrapy==2.11.1
  - openai==1.14.0
  - anthropic==0.21.0
  - psycopg2-binary==2.9.9

### Testing Requirements
- Install base requirements: `pip install -r requirements/base.txt`
- Verify installation: `pip list | grep Django`
- Expected output: Django version 4.2.11

---

## BUXMAX-003: Create Environment Configuration

**Type**: Configuration
**Priority**: Critical  
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-001

### Description
Create `.env.example` file with all required environment variables documented, and set up python-dotenv for loading environment variables.

### Acceptance Criteria
- [ ] `.env.example` file created with 50+ variables
- [ ] All variables documented with comments
- [ ] Variables grouped by category (Django, Database, Redis, AI APIs, Email, Security)
- [ ] Sensitive values use placeholder text
- [ ] `.env` added to `.gitignore`

### Implementation Details
- Reference: enhanced_plan.md Section 15.1 (lines 3938-4010)
- Files to create:
  - `.env.example`
- Files to modify:
  - `.gitignore` (add `.env`)
- Key variables:
  ```bash
  DJANGO_SETTINGS_MODULE=config.settings.development
  SECRET_KEY=your-secret-key-here-min-50-chars
  DEBUG=True
  DATABASE_URL=postgresql://user:password@localhost:5432/buxmax_db
  REDIS_URL=redis://localhost:6379/0
  OPENAI_API_KEY=sk-...
  ANTHROPIC_API_KEY=sk-ant-...
  ```

### Testing Requirements
- Copy to .env: `cp .env.example .env`
- Test loading: Create test script that loads dotenv
- Expected behavior: Variables accessible via os.getenv()

---

## BUXMAX-004: Configure Base Django Settings

**Type**: Configuration
**Priority**: Critical  
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-002, BUXMAX-003

### Description
Create base Django settings file with all core configuration including database, installed apps, middleware, templates, static files, and Celery configuration.

### Acceptance Criteria
- [ ] `config/settings/base.py` created with 200+ lines
- [ ] All INSTALLED_APPS listed (Django defaults + third-party + local apps)
- [ ] Database configuration using environment variables
- [ ] Celery configuration included
- [ ] Cache configuration with Redis
- [ ] Logging configuration included
- [ ] Static and media file settings configured

### Implementation Details
- Reference: enhanced_plan.md Section 15.3.1 (lines 4101-4250)
- Files to create:
  - `config/settings/base.py`
- Key configurations:
  - INSTALLED_APPS: Include django_celery_results, django_celery_beat
  - DATABASES: PostgreSQL with environment variables
  - CACHES: Redis configuration
  - CELERY_BROKER_URL, CELERY_RESULT_BACKEND
  - LOGGING with console and file handlers

### Testing Requirements
- Import settings: `python -c "from config.settings import base"`
- Run check: `python manage.py check --settings=config.settings.base`
- Expected output: No errors (database connection may fail, that's OK)

---

## BUXMAX-005: Configure Development Settings

**Type**: Configuration
**Priority**: High  
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-004

### Description
Create development-specific settings that inherit from base settings and add development tools like Django Debug Toolbar.

### Acceptance Criteria
- [ ] `config/settings/development.py` created
- [ ] Inherits from base.py
- [ ] DEBUG=True set
- [ ] ALLOWED_HOSTS includes localhost
- [ ] Django Debug Toolbar configured
- [ ] Email backend set to console
- [ ] Security settings disabled for development

### Implementation Details
- Reference: enhanced_plan.md Section 15.3.2 (lines 4251-4270)
- Files to create:
  - `config/settings/development.py`
- Key settings:
  ```python
  from .base import *
  DEBUG = True
  ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
  INSTALLED_APPS += ['debug_toolbar']
  MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
  ```

### Testing Requirements
- Set environment: `export DJANGO_SETTINGS_MODULE=config.settings.development`
- Run check: `python manage.py check`
- Start server: `python manage.py runserver`
- Expected behavior: Server starts without errors

---

## BUXMAX-006: Configure Production Settings

**Type**: Configuration
**Priority**: High  
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-004

### Description
Create production-specific settings with security hardening, Sentry integration, and optional AWS S3 configuration.

### Acceptance Criteria
- [ ] `config/settings/production.py` created
- [ ] DEBUG=False enforced
- [ ] All security settings enabled (SSL redirect, secure cookies, HSTS)
- [ ] Sentry SDK configured
- [ ] AWS S3 configuration (conditional)
- [ ] Production-appropriate logging

### Implementation Details
- Reference: enhanced_plan.md Section 15.3.3 (lines 4271-4309)
- Files to create:
  - `config/settings/production.py`
- Key settings:
  ```python
  from .base import *
  DEBUG = False
  SECURE_SSL_REDIRECT = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True
  SECURE_HSTS_SECONDS = 31536000
  ```

### Testing Requirements
- Import settings: `python -c "from config.settings import production"`
- Verify security: Check that all security flags are True
- Expected behavior: No import errors

---

## BUXMAX-007: Create Django Apps

**Type**: Setup
**Priority**: Critical  
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-005

### Description
Create all Django applications (core, aggregation, content, forum, moderation, users) with proper structure including models, views, admin, tests directories.

### Acceptance Criteria
- [ ] Six Django apps created: core, aggregation, content, forum, moderation, users
- [ ] Each app has standard Django files (models.py, views.py, admin.py, urls.py, apps.py)
- [ ] Each app has tests/ directory with __init__.py
- [ ] Each app has templates/ subdirectory
- [ ] All apps added to INSTALLED_APPS in settings

### Implementation Details
- Reference: enhanced_plan.md Section 14.1 (lines 649-891)
- Commands to run:
  ```bash
  cd apps
  python ../manage.py startapp core
  python ../manage.py startapp aggregation
  python ../manage.py startapp content
  python ../manage.py startapp forum
  python ../manage.py startapp moderation
  python ../manage.py startapp users
  ```
- Files to create for each app:
  - `apps/{app_name}/tests/__init__.py`
  - `apps/{app_name}/tests/factories.py`
  - `apps/{app_name}/tests/conftest.py`
  - `apps/{app_name}/templates/{app_name}/`

### Testing Requirements
- Run check: `python manage.py check`
- List apps: `python manage.py showmigrations`
- Expected output: All apps listed, no errors

---

## BUXMAX-008: Setup PostgreSQL Database

**Type**: Setup
**Priority**: Critical  
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-005

### Description
Set up PostgreSQL database locally, create database and user, and verify Django can connect.

### Acceptance Criteria
- [ ] PostgreSQL installed and running
- [ ] Database `buxmax_db` created
- [ ] User `buxmax_user` created with password
- [ ] User has all privileges on database
- [ ] Django can connect to database
- [ ] Database connection parameters in .env file

### Implementation Details
- Reference: enhanced_plan.md Section 15.3.1 (lines 4101-4250)
- Commands to run:
  ```bash
  # PostgreSQL commands
  createdb buxmax_db
  psql -c "CREATE USER buxmax_user WITH PASSWORD 'your_password';"
  psql -c "GRANT ALL PRIVILEGES ON DATABASE buxmax_db TO buxmax_user;"
  ```
- Update .env:
  ```bash
  DB_NAME=buxmax_db
  DB_USER=buxmax_user
  DB_PASSWORD=your_password
  DB_HOST=localhost
  DB_PORT=5432
  ```

### Testing Requirements
- Test connection: `python manage.py dbshell`
- Run migrations: `python manage.py migrate`
- Expected output: Default Django migrations applied successfully

---

## BUXMAX-009: Setup Redis

**Type**: Setup
**Priority**: Critical  
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-005

### Description
Install and configure Redis for use as Celery broker and Django cache backend.

### Acceptance Criteria
- [ ] Redis installed and running
- [ ] Redis accessible on localhost:6379
- [ ] Django cache configured to use Redis
- [ ] Celery broker URL configured
- [ ] Connection verified from Django

### Implementation Details
- Reference: enhanced_plan.md Section 15.3.1 (lines 4101-4250)
- Installation:
  ```bash
  # macOS
  brew install redis
  brew services start redis
  
  # Linux
  sudo apt-get install redis-server
  sudo systemctl start redis
  ```
- Update .env:
  ```bash
  REDIS_URL=redis://localhost:6379/0
  CELERY_BROKER_URL=redis://localhost:6379/0
  CELERY_RESULT_BACKEND=redis://localhost:6379/1
  ```

### Testing Requirements
- Test Redis: `redis-cli ping`
- Expected output: "PONG"
- Test from Django: `python manage.py shell` then:
  ```python
  from django.core.cache import cache
  cache.set('test', 'value')
  print(cache.get('test'))
  ```
- Expected output: "value"

---

## BUXMAX-010: Configure Celery

**Type**: Configuration
**Priority**: Critical  
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-009

### Description
Create Celery configuration file with app initialization, Beat schedule, task routing, and time limits.

### Acceptance Criteria
- [ ] `config/celery.py` created with complete configuration
- [ ] Celery app initialized and configured
- [ ] Beat schedule defined for all periodic tasks
- [ ] Task routing configured (scraping, ai_generation, moderation queues)
- [ ] Time limits set (30 min hard, 25 min soft)
- [ ] Celery worker can start successfully

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.1 (lines 1849-1950)
- Files to create:
  - `config/celery.py`
- Key configuration:
  ```python
  app = Celery('buxmax_gemini')
  app.config_from_object('django.conf:settings', namespace='CELERY')
  app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
  ```
- Beat schedule includes:
  - scrape-due-sources (every 30 min)
  - discover-new-sources (daily at 2 AM)
  - process-pending-content (every 15 min)
  - generate-daily-summary (daily at 8 AM)
  - ai-avatar-scan-topics (hourly)

### Testing Requirements
- Start worker: `celery -A config worker -l info`
- Start beat: `celery -A config beat -l info`
- Expected output: Worker and beat start without errors, tasks discovered

---

# Phase 2: Data Models (BUXMAX-011 to BUXMAX-030)

## BUXMAX-011: Create Core Abstract Models

**Type**: Model
**Priority**: Critical
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-007

### Description
Implement abstract base models (TimeStampedModel, SoftDeleteModel) in the core app that will be inherited by other models throughout the application.

### Acceptance Criteria
- [ ] `TimeStampedModel` created with created_at and updated_at fields
- [ ] `SoftDeleteModel` created with is_deleted and deleted_at fields
- [ ] Both models are abstract (Meta: abstract = True)
- [ ] soft_delete() and restore() methods implemented
- [ ] Models properly documented with docstrings

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.1 (lines 892-930)
- Files to create/modify:
  - `apps/core/models.py`
- Code structure:
  ```python
  class TimeStampedModel(models.Model):
      created_at = models.DateTimeField(auto_now_add=True, db_index=True)
      updated_at = models.DateTimeField(auto_now=True)
      class Meta:
          abstract = True
          ordering = ['-created_at']
  ```

### Testing Requirements
- Create test: `apps/core/tests/test_models.py`
- Test inheritance in a concrete model
- Verify timestamps are auto-populated
- Test soft_delete() and restore() methods
- Run: `pytest apps/core/tests/test_models.py`

---

## BUXMAX-012: Create Source Model

**Type**: Model
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-011

### Description
Implement the Source model with all fields, custom manager, and methods for tracking scraping status and frequency.

### Acceptance Criteria
- [ ] Source model created with 20+ fields
- [ ] All field types, constraints, and indexes match specification
- [ ] SourceManager with active() and due_for_scraping() methods
- [ ] mark_scrape_attempt() method implemented
- [ ] get_effective_url() method implemented
- [ ] Proper Meta class with db_table, ordering, and indexes
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.2 (lines 931-1050)
- Files to create/modify:
  - `apps/aggregation/models.py`
  - `apps/aggregation/admin.py`
- Key fields:
  - url (URLField, unique, max_length=500)
  - source_type (CharField with choices)
  - scrape_frequency (DurationField)
  - status (CharField with choices)
  - target_regions (ArrayField)
- Indexes on: status+last_checked_at, source_type+status

### Testing Requirements
- Create test: `apps/aggregation/tests/test_models.py`
- Test SourceManager.due_for_scraping()
- Test mark_scrape_attempt() updates fields correctly
- Test get_effective_url() returns correct URL
- Run: `pytest apps/aggregation/tests/test_models.py::TestSourceModel`

---

## BUXMAX-013: Create AggregatedContent Model

**Type**: Model
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-012

### Description
Implement AggregatedContent model for storing raw scraped content with content hashing for deduplication.

### Acceptance Criteria
- [ ] AggregatedContent model created with all specified fields
- [ ] ForeignKey relationship to Source
- [ ] content_hash field with unique constraint
- [ ] generate_content_hash() method implemented
- [ ] save() method overridden to auto-generate hash
- [ ] JSONB raw_data field for flexible storage
- [ ] Proper indexes on source+published_at, is_processed+fetched_at
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.2 (lines 1051-1208)
- Files to modify:
  - `apps/aggregation/models.py`
  - `apps/aggregation/admin.py`
- Key implementation:
  ```python
  def generate_content_hash(self):
      content_string = f"{self.url}|{self.title}|{self.content_body[:1000]}"
      return hashlib.sha256(content_string.encode('utf-8')).hexdigest()
  ```

### Testing Requirements
- Test content hash generation
- Test duplicate detection via unique constraint
- Test save() auto-generates hash
- Verify JSONB field stores complex data
- Run: `pytest apps/aggregation/tests/test_models.py::TestAggregatedContentModel`

---

## BUXMAX-014: Create ProcessedContent Model

**Type**: Model
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-013

### Description
Implement ProcessedContent model for storing cleaned and analyzed content with NLP metadata.

### Acceptance Criteria
- [ ] ProcessedContent model created
- [ ] OneToOneField relationship to AggregatedContent
- [ ] Fields for cleaned_title, summary, cleaned_body
- [ ] ArrayField for keywords
- [ ] JSONField for entities
- [ ] sentiment_score, word_count, reading_time_minutes fields
- [ ] calculate_reading_time() method implemented
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.3 (lines 1209-1280)
- Files to modify:
  - `apps/content/models.py`
  - `apps/content/admin.py`
- Key fields:
  - aggregated_content (OneToOneField)
  - keywords (ArrayField of CharField)
  - entities (JSONField)
  - sentiment_score (DecimalField, -1.00 to 1.00)

### Testing Requirements
- Test OneToOne relationship
- Test calculate_reading_time() (200 words/min)
- Test keyword and entity storage
- Run: `pytest apps/content/tests/test_models.py::TestProcessedContentModel`

---

## BUXMAX-015: Create GeneratedArticle Model

**Type**: Model
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-014

### Description
Implement GeneratedArticle model for AI-generated content with cost tracking and publishing workflow.

### Acceptance Criteria
- [ ] GeneratedArticle model created with all fields
- [ ] Slug field with auto-generation from title
- [ ] ManyToMany relationship to ProcessedContent (source_references)
- [ ] ForeignKey to AIAvatar (author_avatar)
- [ ] Generation metadata fields (prompt, model_used, tokens_used, cost)
- [ ] Status field with choices (draft, review, published, archived)
- [ ] publish() method implemented
- [ ] save() overridden to auto-generate slug
- [ ] Model registered in admin with rich text editor

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.3 (lines 1281-1380)
- Files to modify:
  - `apps/content/models.py`
  - `apps/content/admin.py`
- Key implementation:
  ```python
  def publish(self):
      from django.utils import timezone
      self.status = 'published'
      self.published_at = timezone.now()
      self.save(update_fields=['status', 'published_at'])
  ```

### Testing Requirements
- Test slug auto-generation
- Test publish() method
- Test cost tracking fields
- Test ManyToMany relationships
- Run: `pytest apps/content/tests/test_models.py::TestGeneratedArticleModel`

---

## BUXMAX-016: Create Newsletter Model

**Type**: Model
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-015

### Description
Implement Newsletter model for managing email newsletter content and sending status.

### Acceptance Criteria
- [ ] Newsletter model created
- [ ] issue_number field (unique, indexed)
- [ ] issue_date, subject, html_body, text_body fields
- [ ] ManyToMany to GeneratedArticle and ProcessedContent
- [ ] Status field (draft, scheduled, sending, sent, failed)
- [ ] Metrics fields (recipient_count, open_count, click_count)
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.3 (lines 1381-1430)
- Files to modify:
  - `apps/content/models.py`
  - `apps/content/admin.py`
- Key fields:
  - issue_number (IntegerField, unique)
  - status (CharField with choices)
  - scheduled_for, sent_at (DateTimeField)

### Testing Requirements
- Test issue_number uniqueness
- Test ManyToMany relationships
- Test status transitions
- Run: `pytest apps/content/tests/test_models.py::TestNewsletterModel`

---

## BUXMAX-017: Create Comment Model

**Type**: Model
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-015

### Description
Implement Comment model for user comments on generated articles with moderation support.

### Acceptance Criteria
- [ ] Comment model created
- [ ] ForeignKey to GeneratedArticle
- [ ] ForeignKey to User (author)
- [ ] Self-referential ForeignKey for parent (threaded comments)
- [ ] content field (TextField, max_length=5000)
- [ ] moderation_status field with choices
- [ ] moderation_details JSONField
- [ ] Proper indexes on article+moderation_status
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.3 (lines 1431-1511)
- Files to modify:
  - `apps/content/models.py`
  - `apps/content/admin.py`
- Moderation statuses: pending, approved, rejected, flagged_ai, flagged_user

### Testing Requirements
- Test comment creation
- Test threaded comments (parent relationship)
- Test moderation status changes
- Run: `pytest apps/content/tests/test_models.py::TestCommentModel`

---

## BUXMAX-018: Create ForumCategory Model

**Type**: Model
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-011

### Description
Implement ForumCategory model for organizing forum discussions into categories.

### Acceptance Criteria
- [ ] ForumCategory model created
- [ ] name and slug fields (both unique)
- [ ] description field
- [ ] order field for display ordering
- [ ] Metric fields (topic_count, post_count)
- [ ] is_active field
- [ ] save() overridden to auto-generate slug
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.4 (lines 1512-1560)
- Files to create/modify:
  - `apps/forum/models.py`
  - `apps/forum/admin.py`
- Key implementation:
  ```python
  def save(self, *args, **kwargs):
      if not self.slug:
          self.slug = slugify(self.name)
      super().save(*args, **kwargs)
  ```

### Testing Requirements
- Test slug auto-generation
- Test ordering by order field
- Test uniqueness constraints
- Run: `pytest apps/forum/tests/test_models.py::TestForumCategoryModel`

---

## BUXMAX-019: Create ForumTopic Model

**Type**: Model
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-018

### Description
Implement ForumTopic model with GenericForeignKey for creator (User or AIAvatar) and activity tracking.

### Acceptance Criteria
- [ ] ForumTopic model created
- [ ] ForeignKey to ForumCategory
- [ ] GenericForeignKey for creator (User or AIAvatar)
- [ ] title and slug fields
- [ ] Status fields (is_pinned, is_locked)
- [ ] Metric fields (view_count, post_count)
- [ ] Activity tracking (last_post_at, last_post_by GenericForeignKey)
- [ ] Proper indexes on category+last_post_at, is_pinned+last_post_at
- [ ] save() overridden to auto-generate slug
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.4 (lines 1561-1640)
- Files to modify:
  - `apps/forum/models.py`
  - `apps/forum/admin.py`
- GenericForeignKey setup:
  ```python
  from django.contrib.contenttypes.fields import GenericForeignKey
  from django.contrib.contenttypes.models import ContentType

  creator_content_type = models.ForeignKey(ContentType, ...)
  creator_object_id = models.PositiveIntegerField()
  creator = GenericForeignKey('creator_content_type', 'creator_object_id')
  ```

### Testing Requirements
- Test GenericForeignKey with User
- Test GenericForeignKey with AIAvatar (after BUXMAX-022)
- Test activity tracking updates
- Test pinned topics sort first
- Run: `pytest apps/forum/tests/test_models.py::TestForumTopicModel`

---

## BUXMAX-020: Create ForumPost Model

**Type**: Model
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-019

### Description
Implement ForumPost model with GenericForeignKey for author, moderation support, and edit tracking.

### Acceptance Criteria
- [ ] ForumPost model created
- [ ] ForeignKey to ForumTopic
- [ ] GenericForeignKey for author (User or AIAvatar)
- [ ] content field (TextField, max_length=10000)
- [ ] Edit tracking (is_edited, edited_at, edit_reason)
- [ ] moderation_status field with choices
- [ ] moderation_details JSONField
- [ ] like_count field
- [ ] is_by_ai() method implemented
- [ ] Proper indexes on topic+created_at, moderation_status
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.4 (lines 1641-1720)
- Files to modify:
  - `apps/forum/models.py`
  - `apps/forum/admin.py`
- is_by_ai() implementation:
  ```python
  def is_by_ai(self):
      from apps.users.models import AIAvatar
      return isinstance(self.author, AIAvatar)
  ```

### Testing Requirements
- Test post creation by User
- Test post creation by AIAvatar
- Test is_by_ai() method
- Test moderation status changes
- Test edit tracking
- Run: `pytest apps/forum/tests/test_models.py::TestForumPostModel`

---

## BUXMAX-021: Create UserProfile Model

**Type**: Model
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-011

### Description
Implement UserProfile model extending Django User with additional fields and auto-creation via signals.

### Acceptance Criteria
- [ ] UserProfile model created
- [ ] OneToOneField to Django User
- [ ] Profile fields (bio, avatar_url, location, website)
- [ ] interests JSONField
- [ ] Forum activity fields (forum_post_count, forum_topic_count, reputation_score)
- [ ] Newsletter fields (newsletter_subscribed, newsletter_confirmed)
- [ ] Preference fields (email_notifications, show_ai_avatars)
- [ ] post_save signal to auto-create profile
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.5 (lines 1721-1780)
- Files to create/modify:
  - `apps/users/models.py`
  - `apps/users/admin.py`
  - `apps/users/signals.py`
- Signal implementation:
  ```python
  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          UserProfile.objects.create(user=instance)
  ```

### Testing Requirements
- Test profile auto-creation on user creation
- Test profile fields
- Test interests JSONField
- Run: `pytest apps/users/tests/test_models.py::TestUserProfileModel`

---

## BUXMAX-022: Create AIAvatar Model

**Type**: Model
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-011

### Description
Implement AIAvatar model for AI personas with behavior configuration and cooldown logic.

### Acceptance Criteria
- [ ] AIAvatar model created
- [ ] Identity fields (name, slug, avatar_url)
- [ ] Persona fields (persona_description, expertise_areas)
- [ ] Behavior config (generation_rules JSONField, tone, max_posts_per_day, cooldown_minutes)
- [ ] AI config (model_name, temperature, max_tokens)
- [ ] Metric fields (post_count, topic_count, total_tokens_used, total_cost)
- [ ] can_post_in_topic() method with cooldown check
- [ ] is_active field
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.5 (lines 1781-1848)
- Files to modify:
  - `apps/users/models.py`
  - `apps/users/admin.py`
- can_post_in_topic() implementation checks last post time and cooldown_minutes

### Testing Requirements
- Test avatar creation
- Test can_post_in_topic() cooldown logic
- Test expertise_areas JSONField
- Test metric tracking
- Run: `pytest apps/users/tests/test_models.py::TestAIAvatarModel`

---

## BUXMAX-023: Create ModerationRule Model

**Type**: Model
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-011

### Description
Implement ModerationRule model for keyword and regex-based content filtering rules.

### Acceptance Criteria
- [ ] ModerationRule model created
- [ ] name field (unique)
- [ ] rule_type field (keyword, regex, url_pattern)
- [ ] pattern field (TextField)
- [ ] action field (flag, reject, approve)
- [ ] severity field (1-10)
- [ ] is_active field
- [ ] Metric fields (match_count, false_positive_count)
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.6 (lines 1849-1900)
- Files to create/modify:
  - `apps/moderation/models.py`
  - `apps/moderation/admin.py`
- Rule types: keyword, regex, url_pattern
- Actions: flag, reject, approve

### Testing Requirements
- Test rule creation
- Test different rule types
- Test severity ordering
- Run: `pytest apps/moderation/tests/test_models.py::TestModerationRuleModel`

---

## BUXMAX-024: Create ModerationLog Model

**Type**: Model
**Priority**: Medium
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-023

### Description
Implement ModerationLog model using GenericForeignKey to log moderation actions on any content type.

### Acceptance Criteria
- [ ] ModerationLog model created
- [ ] GenericForeignKey for content_object (ForumPost or Comment)
- [ ] action field with choices
- [ ] reason field
- [ ] moderator_user ForeignKey (nullable)
- [ ] moderator_ai boolean field
- [ ] ai_scores JSONField
- [ ] ManyToMany to ModerationRule (matched_rules)
- [ ] timestamp field (auto_now_add)
- [ ] Proper indexes on content_type+object_id, action+timestamp
- [ ] Model registered in admin

### Implementation Details
- Reference: enhanced_plan.md Section 14.2.6 (lines 1901-1970)
- Files to modify:
  - `apps/moderation/models.py`
  - `apps/moderation/admin.py`
- Actions: flagged_ai, flagged_user, approved_auto, approved_human, rejected_auto, rejected_human, edited, deleted

### Testing Requirements
- Test logging for ForumPost
- Test logging for Comment
- Test AI vs human moderator tracking
- Test matched_rules ManyToMany
- Run: `pytest apps/moderation/tests/test_models.py::TestModerationLogModel`

---

## BUXMAX-025: Run Initial Migrations

**Type**: Setup
**Priority**: Critical
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-011 through BUXMAX-024

### Description
Create and run Django migrations for all models created in Phase 2.

### Acceptance Criteria
- [ ] Migrations created for all apps
- [ ] No migration conflicts
- [ ] All migrations run successfully
- [ ] Database schema matches model definitions
- [ ] All indexes created
- [ ] All constraints enforced

### Implementation Details
- Commands to run:
  ```bash
  python manage.py makemigrations core
  python manage.py makemigrations aggregation
  python manage.py makemigrations content
  python manage.py makemigrations forum
  python manage.py makemigrations moderation
  python manage.py makemigrations users
  python manage.py migrate
  ```

### Testing Requirements
- Check migrations: `python manage.py showmigrations`
- Verify schema: `python manage.py dbshell` then `\dt` (PostgreSQL)
- Test model creation: Create instances of each model in Django shell
- Expected output: All migrations applied, no errors

---

## BUXMAX-026: Configure Django Admin for All Models

**Type**: Configuration
**Priority**: Medium
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-025

### Description
Configure Django admin interface for all models with appropriate list displays, filters, search fields, and inline editing where applicable.

### Acceptance Criteria
- [ ] Admin classes created for all 15 models
- [ ] list_display configured with relevant fields
- [ ] list_filter configured for status/type fields
- [ ] search_fields configured for text fields
- [ ] Inlines configured for related models (e.g., Comments on Article)
- [ ] readonly_fields for auto-generated fields
- [ ] Custom actions where appropriate (e.g., bulk approve)
- [ ] All admins registered

### Implementation Details
- Files to modify:
  - `apps/aggregation/admin.py`
  - `apps/content/admin.py`
  - `apps/forum/admin.py`
  - `apps/moderation/admin.py`
  - `apps/users/admin.py`
- Example for Source:
  ```python
  @admin.register(Source)
  class SourceAdmin(admin.ModelAdmin):
      list_display = ['name', 'source_type', 'status', 'last_checked_at']
      list_filter = ['source_type', 'status', 'target_regions']
      search_fields = ['name', 'url']
  ```

### Testing Requirements
- Access admin: `python manage.py createsuperuser` then visit /admin/
- Verify all models appear in admin
- Test list views, filters, and search
- Test creating/editing instances
- Expected behavior: All CRUD operations work smoothly

---

## BUXMAX-027: Create Model Factories for Testing

**Type**: Test
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-025

### Description
Create Factory Boy factories for all models to facilitate test data generation.

### Acceptance Criteria
- [ ] Factory created for each model
- [ ] Factories use appropriate Faker providers
- [ ] SubFactory used for ForeignKey relationships
- [ ] Sequences used for unique fields
- [ ] Factories handle complex fields (JSONField, ArrayField)
- [ ] All factories tested and working

### Implementation Details
- Reference: enhanced_plan.md Section 17.2.2 (lines 4701-4750)
- Files to create:
  - `apps/aggregation/tests/factories.py`
  - `apps/content/tests/factories.py`
  - `apps/forum/tests/factories.py`
  - `apps/moderation/tests/factories.py`
  - `apps/users/tests/factories.py`
- Example:
  ```python
  class SourceFactory(DjangoModelFactory):
      class Meta:
          model = Source
      url = factory.Sequence(lambda n: f'https://example{n}.com')
      name = factory.Faker('company')
  ```

### Testing Requirements
- Test each factory: Create instances and verify fields
- Test relationships: Verify SubFactory creates related objects
- Run: `pytest apps/*/tests/test_factories.py`
- Expected output: All factories create valid model instances

---

## BUXMAX-028: Create Pytest Fixtures

**Type**: Test
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-027

### Description
Create pytest fixtures in conftest.py files for commonly used test data across all apps.

### Acceptance Criteria
- [ ] conftest.py created for each app
- [ ] Fixtures created for common model instances
- [ ] Fixtures use factories for data generation
- [ ] Fixtures properly scoped (function, module, session)
- [ ] Fixtures documented with docstrings

### Implementation Details
- Reference: enhanced_plan.md Section 17.2.3 (lines 4751-4800)
- Files to create:
  - `apps/aggregation/tests/conftest.py`
  - `apps/content/tests/conftest.py`
  - `apps/forum/tests/conftest.py`
  - `apps/moderation/tests/conftest.py`
  - `apps/users/tests/conftest.py`
- Example:
  ```python
  @pytest.fixture
  def source():
      return SourceFactory()

  @pytest.fixture
  def active_sources():
      return SourceFactory.create_batch(5, status='active')
  ```

### Testing Requirements
- Test fixtures: Use in test functions and verify they work
- Run: `pytest apps/aggregation/tests/ -v`
- Expected output: Fixtures available and working

---

## BUXMAX-029: Write Model Unit Tests

**Type**: Test
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-028

### Description
Write comprehensive unit tests for all model methods, properties, and custom managers.

### Acceptance Criteria
- [ ] Test file created for each model
- [ ] Tests for all custom methods
- [ ] Tests for custom managers and querysets
- [ ] Tests for model validation
- [ ] Tests for unique constraints
- [ ] Tests for relationships (ForeignKey, ManyToMany, GenericForeignKey)
- [ ] Test coverage >80% for models
- [ ] All tests passing

### Implementation Details
- Files to create:
  - `apps/aggregation/tests/test_models.py`
  - `apps/content/tests/test_models.py`
  - `apps/forum/tests/test_models.py`
  - `apps/moderation/tests/test_models.py`
  - `apps/users/tests/test_models.py`
- Test structure:
  ```python
  @pytest.mark.django_db
  class TestSourceModel:
      def test_create_source(self, source):
          assert source.id is not None

      def test_due_for_scraping(self):
          # Test SourceManager.due_for_scraping()
  ```

### Testing Requirements
- Run all model tests: `pytest apps/*/tests/test_models.py -v`
- Check coverage: `pytest --cov=apps --cov-report=html`
- Expected output: All tests pass, coverage >80%

---

## BUXMAX-030: Create Database Indexes and Optimize Queries

**Type**: Configuration
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-025

### Description
Review and optimize database indexes for common query patterns, add missing indexes, and verify query performance.

### Acceptance Criteria
- [ ] All indexes from model Meta classes created
- [ ] Composite indexes for common filter combinations
- [ ] GIN indexes for JSONB fields
- [ ] GiST indexes for full-text search (if applicable)
- [ ] Query performance tested with EXPLAIN ANALYZE
- [ ] No missing indexes for foreign keys

### Implementation Details
- Review models and add indexes:
  - Source: (status, last_checked_at), (source_type, status)
  - AggregatedContent: (source_id, published_at), (is_processed, fetched_at)
  - ForumTopic: (category_id, last_post_at), (is_pinned, last_post_at)
  - ForumPost: (topic_id, created_at), (moderation_status)
- Create migration: `python manage.py makemigrations --name add_indexes`

### Testing Requirements
- Check indexes: `python manage.py dbshell` then `\di` (PostgreSQL)
- Test query performance: Use Django Debug Toolbar or EXPLAIN ANALYZE
- Expected output: All indexes present, queries use indexes

---

# Phase 3: Scraping Infrastructure (BUXMAX-031 to BUXMAX-045)

## BUXMAX-031: Initialize Scrapy Project

**Type**: Setup
**Priority**: Critical
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-010

### Description
Initialize Scrapy project within the Django project structure and configure basic settings.

### Acceptance Criteria
- [ ] Scrapy project created in `scrapers/` directory
- [ ] scrapy.cfg file configured
- [ ] Basic directory structure created (spiders/, items.py, pipelines.py, middlewares.py)
- [ ] Scrapy can discover and list spiders
- [ ] Django integration configured

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.1 (lines 2700-2800)
- Commands to run:
  ```bash
  cd scrapers
  scrapy startproject . .
  ```
- Files to create:
  - `scrapers/scrapy.cfg`
  - `scrapers/settings.py`
  - `scrapers/items.py`
  - `scrapers/pipelines.py`
  - `scrapers/middlewares.py`
  - `scrapers/spiders/__init__.py`

### Testing Requirements
- List spiders: `scrapy list`
- Check settings: `scrapy settings --get BOT_NAME`
- Expected output: Scrapy commands work, no errors

---

## BUXMAX-032: Configure Scrapy Settings

**Type**: Configuration
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-031

### Description
Configure Scrapy settings with Django integration, user agent rotation, AutoThrottle, caching, and pipeline configuration.

### Acceptance Criteria
- [ ] Django settings module configured in Scrapy
- [ ] django.setup() called in settings
- [ ] User agent rotation configured
- [ ] AutoThrottle enabled with appropriate settings
- [ ] HTTP caching enabled for development
- [ ] Retry middleware configured
- [ ] All pipelines enabled with priorities
- [ ] Concurrent requests limited appropriately
- [ ] Download delay configured

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.1 (lines 2700-2800)
- Files to modify:
  - `scrapers/settings.py`
- Key settings:
  ```python
  import os
  import django
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
  django.setup()

  BOT_NAME = 'buxmax_scraper'
  ROBOTSTXT_OBEY = True
  CONCURRENT_REQUESTS = 16
  DOWNLOAD_DELAY = 2
  AUTOTHROTTLE_ENABLED = True
  HTTPCACHE_ENABLED = True
  ```

### Testing Requirements
- Verify Django integration: `scrapy shell` then `from apps.aggregation.models import Source`
- Test settings: `scrapy settings --get DOWNLOAD_DELAY`
- Expected output: Django models accessible, settings correct

---

## BUXMAX-033: Create Scrapy Item Definitions

**Type**: Configuration
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-032

### Description
Define Scrapy Item classes for ContentItem and SourceDiscoveryItem with all required fields.

### Acceptance Criteria
- [ ] ContentItem class created with all fields
- [ ] SourceDiscoveryItem class created
- [ ] ItemLoaders defined with input/output processors
- [ ] Field processors for cleaning data (strip whitespace, normalize URLs)
- [ ] Items properly documented

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.2 (lines 2801-2870)
- Files to modify:
  - `scrapers/items.py`
- ContentItem fields:
  ```python
  class ContentItem(scrapy.Item):
      source_id = scrapy.Field()
      url = scrapy.Field()
      title = scrapy.Field()
      content_body = scrapy.Field()
      author = scrapy.Field()
      published_at = scrapy.Field()
      content_type = scrapy.Field()
      raw_data = scrapy.Field()
  ```

### Testing Requirements
- Test item creation: Create ContentItem instance with data
- Test processors: Verify whitespace stripped, URLs normalized
- Run: `pytest scrapers/tests/test_items.py`

---

## BUXMAX-034: Implement Validation Pipeline

**Type**: Spider
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-033

### Description
Implement Scrapy pipeline for validating required fields in scraped items.

### Acceptance Criteria
- [ ] ValidationPipeline class created
- [ ] Checks for required fields (url, title, content_body)
- [ ] Raises DropItem for invalid items
- [ ] Logs validation failures
- [ ] Pipeline enabled in settings with priority 100

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.3 (lines 2871-2920)
- Files to modify:
  - `scrapers/pipelines.py`
  - `scrapers/settings.py` (enable pipeline)
- Implementation:
  ```python
  class ValidationPipeline:
      def process_item(self, item, spider):
          required_fields = ['url', 'title', 'content_body']
          for field in required_fields:
              if not item.get(field):
                  raise DropItem(f"Missing {field} in {item}")
          return item
  ```

### Testing Requirements
- Test with valid item: Should pass through
- Test with missing field: Should raise DropItem
- Run: `pytest scrapers/tests/test_pipelines.py::TestValidationPipeline`

---

## BUXMAX-035: Implement Cleaning Pipeline

**Type**: Spider
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-034

### Description
Implement pipeline for cleaning and normalizing scraped content (HTML cleaning, whitespace normalization, URL normalization).

### Acceptance Criteria
- [ ] CleaningPipeline class created
- [ ] HTML tags stripped from content
- [ ] Whitespace normalized (multiple spaces, newlines)
- [ ] URLs normalized (add scheme, remove fragments)
- [ ] Dates parsed to ISO format
- [ ] Pipeline enabled with priority 200

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.3 (lines 2921-2980)
- Files to modify:
  - `scrapers/pipelines.py`
- Use libraries: BeautifulSoup, bleach, python-dateutil
- Implementation:
  ```python
  class CleaningPipeline:
      def process_item(self, item, spider):
          # Clean HTML
          item['content_body'] = bleach.clean(item['content_body'], strip=True)
          # Normalize whitespace
          item['title'] = ' '.join(item['title'].split())
          # Normalize URL
          item['url'] = self.normalize_url(item['url'])
          return item
  ```

### Testing Requirements
- Test HTML cleaning: Input with tags, verify stripped
- Test whitespace normalization: Multiple spaces become one
- Test URL normalization: Relative URLs become absolute
- Run: `pytest scrapers/tests/test_pipelines.py::TestCleaningPipeline`

---

## BUXMAX-036: Implement Deduplication Pipeline

**Type**: Spider
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-035

### Description
Implement pipeline for detecting and dropping duplicate content based on URL and content hash.

### Acceptance Criteria
- [ ] DeduplicationPipeline class created
- [ ] Checks if URL already exists in database
- [ ] Generates content hash and checks for duplicates
- [ ] Drops duplicate items
- [ ] Logs duplicate detection
- [ ] Pipeline enabled with priority 300

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.3 (lines 2981-3030)
- Files to modify:
  - `scrapers/pipelines.py`
- Implementation:
  ```python
  class DeduplicationPipeline:
      def process_item(self, item, spider):
          from apps.aggregation.models import AggregatedContent
          # Check URL
          if AggregatedContent.objects.filter(url=item['url']).exists():
              raise DropItem(f"Duplicate URL: {item['url']}")
          # Check content hash
          content_hash = self.generate_hash(item)
          if AggregatedContent.objects.filter(content_hash=content_hash).exists():
              raise DropItem(f"Duplicate content: {item['url']}")
          return item
  ```

### Testing Requirements
- Test with new URL: Should pass
- Test with existing URL: Should drop
- Test with duplicate content: Should drop
- Run: `pytest scrapers/tests/test_pipelines.py::TestDeduplicationPipeline`

---

## BUXMAX-037: Implement Django Pipeline

**Type**: Spider
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-036

### Description
Implement pipeline for saving scraped items to Django database (AggregatedContent model).

### Acceptance Criteria
- [ ] DjangoPipeline class created
- [ ] Saves ContentItem to AggregatedContent model
- [ ] Handles database errors gracefully
- [ ] Updates Source.last_checked_at
- [ ] Logs successful saves
- [ ] Pipeline enabled with priority 400

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.3 (lines 3031-3111)
- Files to modify:
  - `scrapers/pipelines.py`
- Implementation:
  ```python
  class DjangoPipeline:
      def process_item(self, item, spider):
          from apps.aggregation.models import AggregatedContent, Source
          try:
              content = AggregatedContent.objects.create(
                  source_id=item['source_id'],
                  url=item['url'],
                  title=item['title'],
                  content_body=item['content_body'],
                  # ... other fields
              )
              spider.logger.info(f"Saved: {content.url}")
          except Exception as e:
              spider.logger.error(f"Error saving: {e}")
          return item
  ```

### Testing Requirements
- Test item save: Verify AggregatedContent created
- Test with invalid data: Should log error, not crash
- Run: `pytest scrapers/tests/test_pipelines.py::TestDjangoPipeline`

---

## BUXMAX-038: Create Base Spider Class

**Type**: Spider
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-037

### Description
Create base spider class with common functionality for all content spiders (error handling, logging, item creation).

### Acceptance Criteria
- [ ] BaseContentSpider class created
- [ ] Inherits from scrapy.Spider
- [ ] Common initialization (source_id, source object)
- [ ] Helper methods for item creation
- [ ] Error handling for parse methods
- [ ] Logging configuration
- [ ] Rate limiting awareness

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.4 (lines 3112-3180)
- Files to create:
  - `scrapers/spiders/base.py`
- Implementation:
  ```python
  class BaseContentSpider(scrapy.Spider):
      def __init__(self, source_id, *args, **kwargs):
          super().__init__(*args, **kwargs)
          from apps.aggregation.models import Source
          self.source = Source.objects.get(id=source_id)
          self.source_id = source_id

      def create_item(self, **kwargs):
          from scrapers.items import ContentItem
          item = ContentItem()
          item['source_id'] = self.source_id
          item.update(kwargs)
          return item
  ```

### Testing Requirements
- Test spider initialization: Verify source loaded
- Test create_item(): Verify item created with source_id
- Run: `pytest scrapers/tests/test_spiders.py::TestBaseContentSpider`

---

## BUXMAX-039: Implement RSS Spider

**Type**: Spider
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-038

### Description
Implement spider for scraping RSS and Atom feeds using feedparser library.

### Acceptance Criteria
- [ ] RSSSpider class created, inherits from BaseContentSpider
- [ ] Parses RSS 2.0 feeds
- [ ] Parses Atom feeds
- [ ] Extracts title, link, description, author, published date
- [ ] Handles missing fields gracefully
- [ ] Handles malformed feeds
- [ ] Spider registered and discoverable

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.4 (lines 3181-3250)
- Files to create:
  - `scrapers/spiders/rss_spider.py`
- Implementation:
  ```python
  class RSSSpider(BaseContentSpider):
      name = 'rss'

      def parse(self, response):
          import feedparser
          feed = feedparser.parse(response.text)
          for entry in feed.entries:
              yield self.create_item(
                  url=entry.link,
                  title=entry.title,
                  content_body=entry.get('description', ''),
                  author=entry.get('author', ''),
                  published_at=entry.get('published', ''),
              )
  ```

### Testing Requirements
- Test with sample RSS feed: `scrapers/tests/fixtures/sample_rss.xml`
- Test with sample Atom feed: `scrapers/tests/fixtures/sample_atom.xml`
- Verify items extracted correctly
- Run: `pytest scrapers/tests/test_spiders.py::TestRSSSpider`

---

## BUXMAX-040: Implement Blog Spider

**Type**: Spider
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-038

### Description
Implement generic blog spider for scraping HTML blog posts with automatic content extraction.

### Acceptance Criteria
- [ ] BlogSpider class created
- [ ] Follows links to article pages
- [ ] Extracts article content using heuristics
- [ ] Handles various blog layouts
- [ ] Extracts metadata (author, date, tags)
- [ ] Respects robots.txt
- [ ] Handles pagination
- [ ] Spider registered and discoverable

### Implementation Details
- Reference: enhanced_plan.md Section 14.4.4 (lines 3251-3318)
- Files to create:
  - `scrapers/spiders/blog_spider.py`
- Use libraries: BeautifulSoup, newspaper3k (optional)
- Implementation:
  ```python
  class BlogSpider(BaseContentSpider):
      name = 'blog'

      def parse(self, response):
          # Extract article links
          for link in response.css('a.article-link::attr(href)').getall():
              yield response.follow(link, self.parse_article)

      def parse_article(self, response):
          # Extract article content
          yield self.create_item(
              url=response.url,
              title=response.css('h1.title::text').get(),
              content_body=response.css('div.content').get(),
              # ...
          )
  ```

### Testing Requirements
- Test with sample HTML pages
- Test link following
- Test content extraction
- Run: `pytest scrapers/tests/test_spiders.py::TestBlogSpider`

---

## BUXMAX-041: Create Scraper Service

**Type**: API Integration
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-040

### Description
Create ScraperService class to manage spider execution from Django/Celery, handle results, and update source status.

### Acceptance Criteria
- [ ] ScraperService class created in aggregation app
- [ ] scrape_source() method executes appropriate spider
- [ ] Handles spider selection based on source_type
- [ ] Captures spider statistics (items scraped, errors)
- [ ] Updates Source model after scraping
- [ ] Handles spider errors gracefully
- [ ] Returns structured result dictionary

### Implementation Details
- Files to create:
  - `apps/aggregation/services.py`
- Implementation:
  ```python
  class ScraperService:
      def scrape_source(self, source_id):
          from scrapy.crawler import CrawlerProcess
          from scrapers.spiders.rss_spider import RSSSpider

          source = Source.objects.get(id=source_id)

          # Select spider based on source_type
          spider_class = self.get_spider_class(source.source_type)

          # Run spider
          process = CrawlerProcess(get_project_settings())
          process.crawl(spider_class, source_id=source_id)
          process.start()

          # Update source
          source.mark_scrape_attempt(success=True)

          return {'success': True, 'items_scraped': 10}
  ```

### Testing Requirements
- Test scrape_source() with mock spider
- Test spider selection logic
- Test source status updates
- Run: `pytest apps/aggregation/tests/test_services.py::TestScraperService`

---

## BUXMAX-042: Implement User Agent Rotation Middleware

**Type**: Spider
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-032

### Description
Implement Scrapy middleware for rotating user agents to avoid detection and blocking.

### Acceptance Criteria
- [ ] UserAgentRotationMiddleware class created
- [ ] List of 10+ realistic user agents
- [ ] Random user agent selected for each request
- [ ] Middleware enabled in settings
- [ ] Logs user agent changes (debug level)

### Implementation Details
- Files to modify:
  - `scrapers/middlewares.py`
  - `scrapers/settings.py`
- Implementation:
  ```python
  class UserAgentRotationMiddleware:
      def __init__(self):
          self.user_agents = [
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...',
              # ... more user agents
          ]

      def process_request(self, request, spider):
          request.headers['User-Agent'] = random.choice(self.user_agents)
  ```

### Testing Requirements
- Test middleware: Verify user agent changes
- Test with spider: Check request headers
- Run: `pytest scrapers/tests/test_middlewares.py`

---

## BUXMAX-043: Create Spider Tests

**Type**: Test
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-040

### Description
Write comprehensive tests for all spiders using mock HTTP responses and fixtures.

### Acceptance Criteria
- [ ] Test file created for each spider
- [ ] Fixture files created (sample RSS, HTML pages)
- [ ] Tests for successful scraping
- [ ] Tests for error handling
- [ ] Tests for edge cases (missing fields, malformed data)
- [ ] All tests passing

### Implementation Details
- Reference: enhanced_plan.md Section 17.3.2 (lines 4801-4850)
- Files to create:
  - `scrapers/tests/test_spiders.py`
  - `scrapers/tests/fixtures/sample_rss.xml`
  - `scrapers/tests/fixtures/sample_blog.html`
- Use fake_response_from_file() helper

### Testing Requirements
- Run all spider tests: `pytest scrapers/tests/test_spiders.py -v`
- Expected output: All tests pass

---

## BUXMAX-044: Create Pipeline Tests

**Type**: Test
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-037

### Description
Write tests for all Scrapy pipelines to ensure proper validation, cleaning, deduplication, and saving.

### Acceptance Criteria
- [ ] Test file created for pipelines
- [ ] Tests for ValidationPipeline
- [ ] Tests for CleaningPipeline
- [ ] Tests for DeduplicationPipeline
- [ ] Tests for DjangoPipeline
- [ ] All tests passing

### Implementation Details
- Files to create:
  - `scrapers/tests/test_pipelines.py`
- Test structure:
  ```python
  @pytest.mark.django_db
  class TestDjangoPipeline:
      def test_saves_item(self, source):
          pipeline = DjangoPipeline()
          item = ContentItem(source_id=source.id, ...)
          pipeline.process_item(item, None)
          assert AggregatedContent.objects.filter(url=item['url']).exists()
  ```

### Testing Requirements
- Run: `pytest scrapers/tests/test_pipelines.py -v`
- Expected output: All tests pass

---

## BUXMAX-045: Create Scraping Documentation

**Type**: Documentation
**Priority**: Low
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-044

### Description
Create comprehensive documentation for the scraping infrastructure including spider usage, adding new sources, and troubleshooting.

### Acceptance Criteria
- [ ] Documentation file created
- [ ] Spider usage examples
- [ ] How to add new source types
- [ ] How to create custom spiders
- [ ] Troubleshooting common issues
- [ ] Configuration reference

### Implementation Details
- Files to create:
  - `docs/scraping_guide.md`
- Sections:
  - Overview of scraping architecture
  - Available spiders and when to use them
  - Adding new sources via admin
  - Creating custom spiders
  - Pipeline configuration
  - Testing spiders
  - Common errors and solutions

### Testing Requirements
- Review documentation for completeness
- Verify all examples work
- Expected output: Clear, comprehensive documentation

---

# Phase 4: Celery Tasks (BUXMAX-046 to BUXMAX-060)

## BUXMAX-046: Implement scrape_source Task

**Type**: Task
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-041

### Description
Implement Celery task for scraping a single source with retry logic and error handling.

### Acceptance Criteria
- [ ] scrape_source task created in aggregation app
- [ ] Task decorated with @shared_task
- [ ] Retry configuration (max_retries=3, exponential backoff)
- [ ] Calls ScraperService.scrape_source()
- [ ] Updates Source.last_checked_at
- [ ] Handles and logs errors
- [ ] Returns structured result
- [ ] Task routed to 'scraping' queue

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.2 (lines 1951-2020)
- Files to create:
  - `apps/aggregation/tasks.py`
- Implementation:
  ```python
  @shared_task(bind=True, max_retries=3, autoretry_for=(Exception,))
  def scrape_source(self, source_id: int) -> Dict[str, any]:
      try:
          service = ScraperService()
          result = service.scrape_source(source_id)
          return result
      except Exception as exc:
          logger.error(f"Error scraping source {source_id}: {exc}")
          raise self.retry(exc=exc, countdown=60 * (2 ** self.request.retries))
  ```

### Testing Requirements
- Test task execution: `scrape_source.delay(source_id)`
- Test with mock ScraperService
- Test retry logic
- Run: `pytest apps/aggregation/tests/test_tasks.py::test_scrape_source`

---

## BUXMAX-047: Implement scrape_due_sources Task

**Type**: Task
**Priority**: Critical
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-046

### Description
Implement periodic Celery task that finds sources due for scraping and dispatches scrape_source tasks.

### Acceptance Criteria
- [ ] scrape_due_sources task created
- [ ] Queries Source.objects.due_for_scraping()
- [ ] Dispatches scrape_source.delay() for each source
- [ ] Logs number of sources dispatched
- [ ] Configured in Celery Beat schedule (every 30 min)
- [ ] Returns count of dispatched tasks

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.2 (lines 2021-2070)
- Files to modify:
  - `apps/aggregation/tasks.py`
  - `config/celery.py` (add to beat_schedule)
- Implementation:
  ```python
  @shared_task
  def scrape_due_sources() -> Dict[str, int]:
      sources = Source.objects.due_for_scraping()
      count = 0
      for source in sources:
          scrape_source.delay(source.id)
          count += 1
      logger.info(f"Dispatched {count} scraping tasks")
      return {'dispatched': count}
  ```

### Testing Requirements
- Test with due sources: Verify tasks dispatched
- Test with no due sources: Should return 0
- Run: `pytest apps/aggregation/tests/test_tasks.py::test_scrape_due_sources`

---

## BUXMAX-048: Implement discover_new_sources Task

**Type**: Task
**Priority**: Medium
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-047

### Description
Implement task for discovering new frugal living sources through search and link analysis.

### Acceptance Criteria
- [ ] discover_new_sources task created
- [ ] Searches for frugal living blogs/sites
- [ ] Analyzes existing source links for new sources
- [ ] Validates discovered sources (checks robots.txt, content quality)
- [ ] Creates Source entries with status='pending'
- [ ] Avoids duplicates
- [ ] Configured in Beat schedule (daily at 2 AM)
- [ ] Returns count of discovered sources

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.2 (lines 2071-2150)
- Files to modify:
  - `apps/aggregation/tasks.py`
- Implementation approach:
  - Use Google Custom Search API or similar
  - Extract links from existing aggregated content
  - Check if URL already exists
  - Validate source (fetch robots.txt, sample content)
  - Create Source with status='pending'

### Testing Requirements
- Test with mock search results
- Test duplicate detection
- Test source validation
- Run: `pytest apps/aggregation/tests/test_tasks.py::test_discover_new_sources`

---

## BUXMAX-049: Implement process_aggregated_content Task

**Type**: Task
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-046

### Description
Implement task for processing raw aggregated content (cleaning, NLP analysis, keyword extraction).

### Acceptance Criteria
- [ ] process_aggregated_content task created
- [ ] Fetches AggregatedContent by ID
- [ ] Cleans HTML and text
- [ ] Extracts keywords using NLP
- [ ] Performs sentiment analysis
- [ ] Calculates reading time
- [ ] Creates ProcessedContent entry
- [ ] Marks AggregatedContent as processed
- [ ] Task routed to 'default' queue

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.3 (lines 2151-2230)
- Files to create:
  - `apps/content/tasks.py`
  - `apps/content/services.py` (ContentProcessingService)
- Implementation:
  ```python
  @shared_task(bind=True, max_retries=2)
  def process_aggregated_content(self, content_id: int):
      content = AggregatedContent.objects.get(id=content_id)
      service = ContentProcessingService()
      processed = service.process_content(content)
      content.is_processed = True
      content.save()
      return {'processed_id': processed.id}
  ```

### Testing Requirements
- Test content processing
- Test keyword extraction
- Test sentiment analysis
- Run: `pytest apps/content/tests/test_tasks.py::test_process_aggregated_content`

---

## BUXMAX-050: Implement process_pending_content Task

**Type**: Task
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-049

### Description
Implement periodic task that finds unprocessed aggregated content and dispatches processing tasks.

### Acceptance Criteria
- [ ] process_pending_content task created
- [ ] Queries AggregatedContent.objects.filter(is_processed=False)
- [ ] Limits to batch size (e.g., 50 items)
- [ ] Dispatches process_aggregated_content.delay() for each
- [ ] Configured in Beat schedule (every 15 min)
- [ ] Returns count of dispatched tasks

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.3 (lines 2231-2280)
- Files to modify:
  - `apps/content/tasks.py`
- Implementation:
  ```python
  @shared_task
  def process_pending_content() -> Dict[str, int]:
      pending = AggregatedContent.objects.filter(
          is_processed=False
      ).order_by('fetched_at')[:50]

      count = 0
      for content in pending:
          process_aggregated_content.delay(content.id)
          count += 1
      return {'dispatched': count}
  ```

### Testing Requirements
- Test with pending content
- Test batch limiting
- Run: `pytest apps/content/tests/test_tasks.py::test_process_pending_content`

---

## BUXMAX-051: Implement generate_article Task

**Type**: Task
**Priority**: Critical
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-050

### Description
Implement task for generating AI articles from processed content using LLM APIs.

### Acceptance Criteria
- [ ] generate_article task created
- [ ] Accepts topic and source_content_ids
- [ ] Builds prompt from source content
- [ ] Calls AI client (OpenAI or Anthropic)
- [ ] Creates GeneratedArticle entry
- [ ] Links source_references
- [ ] Tracks tokens and cost
- [ ] Handles API errors with retry
- [ ] Task routed to 'ai_generation' queue

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.3 (lines 2281-2360)
- Files to modify:
  - `apps/content/tasks.py`
  - `apps/content/services.py` (AIGenerationService)
- Implementation:
  ```python
  @shared_task(bind=True, max_retries=2)
  def generate_article(self, topic: str, source_content_ids: List[int]):
      service = AIGenerationService()
      article = service.generate_article(topic, source_content_ids)
      return {'article_id': article.id, 'cost': float(article.generation_cost)}
  ```

### Testing Requirements
- Test with mock AI client
- Test prompt building
- Test cost tracking
- Run: `pytest apps/content/tests/test_tasks.py::test_generate_article`

---

## BUXMAX-052: Implement generate_daily_summary Task

**Type**: Task
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-051

### Description
Implement task that generates daily summary article from top processed content of the day.

### Acceptance Criteria
- [ ] generate_daily_summary task created
- [ ] Queries ProcessedContent from last 24 hours
- [ ] Selects top 20 items by relevance/quality
- [ ] Dispatches generate_article task
- [ ] Configured in Beat schedule (daily at 8 AM)
- [ ] Returns article ID

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.3 (lines 2361-2420)
- Files to modify:
  - `apps/content/tasks.py`
- Implementation:
  ```python
  @shared_task(bind=True)
  def generate_daily_summary(self):
      from django.utils import timezone
      from datetime import timedelta

      yesterday = timezone.now() - timedelta(days=1)
      content = ProcessedContent.objects.filter(
          created_at__gte=yesterday
      ).order_by('-aggregated_content__source__relevance_score')[:20]

      content_ids = [c.id for c in content]
      topic = f"Frugal Living Roundup - {timezone.now().strftime('%Y-%m-%d')}"

      result = generate_article.delay(topic, content_ids)
      return {'task_id': result.id}
  ```

### Testing Requirements
- Test content selection
- Test with no content (should handle gracefully)
- Run: `pytest apps/content/tests/test_tasks.py::test_generate_daily_summary`

---

## BUXMAX-053: Implement generate_weekly_newsletter Task

**Type**: Task
**Priority**: Medium
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-052

### Description
Implement task for generating weekly newsletter content from best articles and content of the week.

### Acceptance Criteria
- [ ] generate_weekly_newsletter task created
- [ ] Queries GeneratedArticle and ProcessedContent from last 7 days
- [ ] Selects top content by engagement/quality
- [ ] Generates newsletter HTML and text versions
- [ ] Creates Newsletter entry
- [ ] Configured in Beat schedule (weekly, Sunday 6 AM)
- [ ] Returns newsletter ID

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.3 (lines 2421-2480)
- Files to modify:
  - `apps/content/tasks.py`
  - `apps/content/services.py` (NewsletterService)
- Implementation:
  ```python
  @shared_task(bind=True)
  def generate_weekly_newsletter(self):
      service = NewsletterService()
      newsletter = service.generate_newsletter(
          period='week',
          issue_number=self.get_next_issue_number()
      )
      return {'newsletter_id': newsletter.id}
  ```

### Testing Requirements
- Test newsletter generation
- Test HTML/text rendering
- Run: `pytest apps/content/tests/test_tasks.py::test_generate_weekly_newsletter`

---

## BUXMAX-054: Implement send_newsletter Task

**Type**: Task
**Priority**: Medium
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-053

### Description
Implement task for sending newsletter emails to subscribers with tracking.

### Acceptance Criteria
- [ ] send_newsletter task created
- [ ] Fetches Newsletter by ID
- [ ] Queries subscribed users
- [ ] Sends emails in batches
- [ ] Tracks sending status
- [ ] Updates Newsletter metrics
- [ ] Handles email errors gracefully
- [ ] Returns send statistics

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.3 (lines 2481-2550)
- Files to modify:
  - `apps/content/tasks.py`
- Implementation:
  ```python
  @shared_task(bind=True)
  def send_newsletter(self, newsletter_id: int):
      newsletter = Newsletter.objects.get(id=newsletter_id)
      subscribers = UserProfile.objects.filter(
          newsletter_subscribed=True,
          newsletter_confirmed=True
      )

      sent_count = 0
      for subscriber in subscribers:
          try:
              send_mail(
                  subject=newsletter.subject,
                  message=newsletter.text_body,
                  html_message=newsletter.html_body,
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[subscriber.user.email]
              )
              sent_count += 1
          except Exception as e:
              logger.error(f"Error sending to {subscriber.user.email}: {e}")

      newsletter.recipient_count = sent_count
      newsletter.status = 'sent'
      newsletter.save()
      return {'sent': sent_count}
  ```

### Testing Requirements
- Test with mock email backend
- Test batch sending
- Test error handling
- Run: `pytest apps/content/tests/test_tasks.py::test_send_newsletter`

---

## BUXMAX-055: Implement ai_avatar_respond_to_mention Task

**Type**: Task
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-051

### Description
Implement task for AI avatar to respond to mentions in forum posts.

### Acceptance Criteria
- [ ] ai_avatar_respond_to_mention task created
- [ ] Fetches ForumPost and AIAvatar
- [ ] Checks cooldown with can_post_in_topic()
- [ ] Builds context from topic and recent posts
- [ ] Generates response using AI client
- [ ] Creates ForumPost with AIAvatar as author
- [ ] Updates avatar metrics
- [ ] Task routed to 'ai_generation' queue

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.4 (lines 2551-2630)
- Files to create:
  - `apps/forum/tasks.py`
  - `apps/forum/services.py` (AIAvatarService)
- Implementation:
  ```python
  @shared_task(bind=True, max_retries=2)
  def ai_avatar_respond_to_mention(self, post_id: int, avatar_id: int):
      post = ForumPost.objects.get(id=post_id)
      avatar = AIAvatar.objects.get(id=avatar_id)

      if not avatar.can_post_in_topic(post.topic):
          return {'skipped': 'cooldown'}

      service = AIAvatarService()
      response = service.generate_response(avatar, post)

      return {'post_id': response.id}
  ```

### Testing Requirements
- Test with mock AI client
- Test cooldown logic
- Test response generation
- Run: `pytest apps/forum/tests/test_tasks.py::test_ai_avatar_respond_to_mention`

---

## BUXMAX-056: Implement ai_avatar_initiate_topic Task

**Type**: Task
**Priority**: Medium
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-055

### Description
Implement task for AI avatar to proactively create new forum topics based on recent content.

### Acceptance Criteria
- [ ] ai_avatar_initiate_topic task created
- [ ] Selects AIAvatar and ForumCategory
- [ ] Finds relevant recent content
- [ ] Generates topic title and initial post
- [ ] Creates ForumTopic and ForumPost
- [ ] Updates avatar metrics
- [ ] Respects max_posts_per_day limit

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.4 (lines 2631-2690)
- Files to modify:
  - `apps/forum/tasks.py`
- Implementation:
  ```python
  @shared_task(bind=True)
  def ai_avatar_initiate_topic(self, avatar_id: int, category_id: int):
      avatar = AIAvatar.objects.get(id=avatar_id)
      category = ForumCategory.objects.get(id=category_id)

      # Check daily limit
      if avatar.has_reached_daily_limit():
          return {'skipped': 'daily_limit'}

      service = AIAvatarService()
      topic = service.create_topic(avatar, category)

      return {'topic_id': topic.id}
  ```

### Testing Requirements
- Test topic creation
- Test daily limit enforcement
- Run: `pytest apps/forum/tests/test_tasks.py::test_ai_avatar_initiate_topic`

---

## BUXMAX-057: Implement ai_avatar_scan_and_participate Task

**Type**: Task
**Priority**: Medium
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-056

### Description
Implement periodic task for AI avatars to scan active topics and participate where relevant.

### Acceptance Criteria
- [ ] ai_avatar_scan_and_participate task created
- [ ] Queries active AIAvatars
- [ ] Finds topics matching avatar expertise
- [ ] Checks if avatar should participate (relevance, cooldown)
- [ ] Dispatches response tasks
- [ ] Configured in Beat schedule (hourly)
- [ ] Returns participation count

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.4 (lines 2691-2750)
- Files to modify:
  - `apps/forum/tasks.py`
- Implementation:
  ```python
  @shared_task
  def ai_avatar_scan_and_participate():
      avatars = AIAvatar.objects.filter(is_active=True)
      participation_count = 0

      for avatar in avatars:
          topics = ForumTopic.objects.filter(
              category__name__in=avatar.expertise_areas
          ).order_by('-last_post_at')[:10]

          for topic in topics:
              if avatar.should_participate(topic):
                  ai_avatar_respond_to_mention.delay(topic.id, avatar.id)
                  participation_count += 1

      return {'participated': participation_count}
  ```

### Testing Requirements
- Test topic selection
- Test participation logic
- Run: `pytest apps/forum/tests/test_tasks.py::test_ai_avatar_scan_and_participate`

---

## BUXMAX-058: Implement moderate_content Task

**Type**: Task
**Priority**: Critical
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-051

### Description
Implement task for automated content moderation using keyword rules and AI analysis.

### Acceptance Criteria
- [ ] moderate_content task created
- [ ] Accepts content_type and content_id
- [ ] Layer 1: Checks keyword/regex rules
- [ ] Layer 2: AI analysis for borderline content
- [ ] Layer 3: Decision logic (approve/reject/flag)
- [ ] Creates ModerationLog entry
- [ ] Updates content moderation_status
- [ ] Task routed to 'moderation' queue

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.5 (lines 2751-2850)
- Files to create:
  - `apps/moderation/tasks.py`
  - `apps/moderation/services.py` (ModerationService)
- Implementation:
  ```python
  @shared_task(bind=True, max_retries=2)
  def moderate_content(self, content_type: str, content_id: int):
      service = ModerationService()
      result = service.moderate(content_type, content_id)
      return result
  ```

### Testing Requirements
- Test keyword matching
- Test AI moderation (with mock)
- Test decision logic
- Run: `pytest apps/moderation/tests/test_tasks.py::test_moderate_content`

---

## BUXMAX-059: Implement escalate_old_flagged_content Task

**Type**: Task
**Priority**: Low
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-058

### Description
Implement periodic task to escalate flagged content that hasn't been reviewed by humans.

### Acceptance Criteria
- [ ] escalate_old_flagged_content task created
- [ ] Queries content flagged >24 hours ago
- [ ] Sends notification to moderators
- [ ] Updates escalation status
- [ ] Configured in Beat schedule (daily)
- [ ] Returns escalation count

### Implementation Details
- Reference: enhanced_plan.md Section 14.3.5 (lines 2851-2900)
- Files to modify:
  - `apps/moderation/tasks.py`
- Implementation:
  ```python
  @shared_task
  def escalate_old_flagged_content():
      from django.utils import timezone
      from datetime import timedelta

      threshold = timezone.now() - timedelta(hours=24)
      old_flags = ModerationLog.objects.filter(
          action='flagged_ai',
          timestamp__lt=threshold,
          resolved=False
      )

      for log in old_flags:
          # Send notification
          notify_moderators(log)

      return {'escalated': old_flags.count()}
  ```

### Testing Requirements
- Test with old flagged content
- Test notification sending
- Run: `pytest apps/moderation/tests/test_tasks.py::test_escalate_old_flagged_content`

---

## BUXMAX-060: Create Task Tests

**Type**: Test
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-059

### Description
Write comprehensive tests for all Celery tasks with mocked dependencies.

### Acceptance Criteria
- [ ] Test file created for each task module
- [ ] Tests for successful execution
- [ ] Tests for error handling and retries
- [ ] Tests for task chaining
- [ ] Tests with mocked external services
- [ ] All tests passing
- [ ] Test coverage >80% for tasks

### Implementation Details
- Reference: enhanced_plan.md Section 17.3.3 (lines 4851-4920)
- Files to create:
  - `apps/aggregation/tests/test_tasks.py`
  - `apps/content/tests/test_tasks.py`
  - `apps/forum/tests/test_tasks.py`
  - `apps/moderation/tests/test_tasks.py`
- Use @patch decorator for mocking

### Testing Requirements
- Run all task tests: `pytest apps/*/tests/test_tasks.py -v`
- Check coverage: `pytest --cov=apps --cov-report=html`
- Expected output: All tests pass, coverage >80%

---

# Phase 5: AI Integration (BUXMAX-061 to BUXMAX-070)

## BUXMAX-061: Implement Base AI Client

**Type**: API Integration
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-010

### Description
Create abstract base class for AI clients with common functionality (rate limiting, retry logic, usage tracking).

### Acceptance Criteria
- [ ] BaseAIClient abstract class created
- [ ] Rate limiting using Redis cache
- [ ] Retry logic with exponential backoff
- [ ] Usage tracking (tokens, cost)
- [ ] Error handling for API failures
- [ ] Logging for all API calls
- [ ] Abstract generate() method

### Implementation Details
- Reference: enhanced_plan.md Section 14.5.1 (lines 3319-3400)
- Files to create:
  - `apps/content/ai_clients.py`
- Implementation:
  ```python
  class BaseAIClient(ABC):
      def __init__(self, model: str):
          self.model = model
          self.cache = cache

      def check_rate_limit(self):
          # Check Redis cache for rate limit

      @abstractmethod
      def generate(self, prompt: str, **kwargs):
          pass
  ```

### Testing Requirements
- Test rate limiting
- Test retry logic
- Run: `pytest apps/content/tests/test_ai_clients.py::TestBaseAIClient`

---

## BUXMAX-062: Implement OpenAI Client

**Type**: API Integration
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-061

### Description
Implement OpenAI API client wrapper with GPT-4o support, token tracking, and cost calculation.

### Acceptance Criteria
- [ ] OpenAIClient class created, inherits from BaseAIClient
- [ ] generate() method implemented
- [ ] Supports GPT-4o and GPT-4o-mini models
- [ ] Token usage tracking
- [ ] Cost calculation (per 1M tokens)
- [ ] Error handling for API errors
- [ ] Streaming support (optional)

### Implementation Details
- Reference: enhanced_plan.md Section 14.5.1 (lines 3401-3480)
- Files to modify:
  - `apps/content/ai_clients.py`
- Implementation:
  ```python
  class OpenAIClient(BaseAIClient):
      PRICING = {
          'gpt-4o': {'input': 2.50, 'output': 10.00},
          'gpt-4o-mini': {'input': 0.15, 'output': 0.60}
      }

      def generate(self, prompt, system_prompt=None, temperature=0.7, max_tokens=2000):
          from openai import OpenAI
          client = OpenAI(api_key=settings.OPENAI_API_KEY)

          response = client.chat.completions.create(
              model=self.model,
              messages=[
                  {"role": "system", "content": system_prompt},
                  {"role": "user", "content": prompt}
              ],
              temperature=temperature,
              max_tokens=max_tokens
          )

          return {
              'text': response.choices[0].message.content,
              'tokens_used': response.usage.total_tokens,
              'cost': self.calculate_cost(response.usage),
              'model': self.model
          }
  ```

### Testing Requirements
- Test with mock OpenAI API
- Test cost calculation
- Test error handling
- Run: `pytest apps/content/tests/test_ai_clients.py::TestOpenAIClient`

---

## BUXMAX-063: Implement Anthropic Client

**Type**: API Integration
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-061

### Description
Implement Anthropic API client wrapper with Claude 3.5 Sonnet support.

### Acceptance Criteria
- [ ] AnthropicClient class created
- [ ] generate() method implemented
- [ ] Supports Claude 3.5 Sonnet model
- [ ] Token usage tracking
- [ ] Cost calculation
- [ ] Error handling

### Implementation Details
- Reference: enhanced_plan.md Section 14.5.1 (lines 3481-3523)
- Files to modify:
  - `apps/content/ai_clients.py`
- Similar structure to OpenAIClient but using Anthropic SDK

### Testing Requirements
- Test with mock Anthropic API
- Test cost calculation
- Run: `pytest apps/content/tests/test_ai_clients.py::TestAnthropicClient`

---

## BUXMAX-064: Create Prompt Templates

**Type**: Configuration
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-063

### Description
Create prompt templates for different AI generation tasks (articles, summaries, forum responses).

### Acceptance Criteria
- [ ] Prompt template file created
- [ ] Templates for article generation
- [ ] Templates for daily summaries
- [ ] Templates for forum responses
- [ ] Templates for moderation analysis
- [ ] Templates use Jinja2 or similar for variable substitution
- [ ] Templates documented with usage examples

### Implementation Details
- Files to create:
  - `apps/content/prompts.py`
- Example:
  ```python
  ARTICLE_GENERATION_PROMPT = """
  You are a frugal living expert. Generate a comprehensive article on the following topic:

  Topic: {topic}

  Source Content:
  {source_content}

  Requirements:
  - 800-1200 words
  - Practical, actionable advice
  - Include specific examples
  - Maintain friendly, encouraging tone
  """
  ```

### Testing Requirements
- Test template rendering with sample data
- Verify all variables substituted correctly
- Run: `pytest apps/content/tests/test_prompts.py`

---

## BUXMAX-065: Implement AIGenerationService

**Type**: API Integration
**Priority**: Critical
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-064

### Description
Create service class for AI content generation with prompt building, client selection, and result processing.

### Acceptance Criteria
- [ ] AIGenerationService class created
- [ ] generate_article() method implemented
- [ ] generate_summary() method implemented
- [ ] build_prompt() helper method
- [ ] Client selection logic (OpenAI vs Anthropic)
- [ ] Result processing and validation
- [ ] Error handling and fallback

### Implementation Details
- Files to create/modify:
  - `apps/content/services.py`
- Implementation:
  ```python
  class AIGenerationService:
      def generate_article(self, topic, source_content_ids):
          # Fetch source content
          sources = ProcessedContent.objects.filter(id__in=source_content_ids)

          # Build prompt
          prompt = self.build_article_prompt(topic, sources)

          # Select client
          client = OpenAIClient(model='gpt-4o')

          # Generate
          result = client.generate(prompt, temperature=0.7)

          # Create article
          article = GeneratedArticle.objects.create(
              title=topic,
              body=result['text'],
              tokens_used=result['tokens_used'],
              generation_cost=result['cost'],
              # ...
          )

          return article
  ```

### Testing Requirements
- Test with mock AI client
- Test prompt building
- Test article creation
- Run: `pytest apps/content/tests/test_services.py::TestAIGenerationService`

---

## BUXMAX-066: Implement ContentProcessingService

**Type**: API Integration
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-014

### Description
Create service for processing aggregated content (cleaning, keyword extraction, sentiment analysis).

### Acceptance Criteria
- [ ] ContentProcessingService class created
- [ ] process_content() method implemented
- [ ] HTML cleaning with bleach
- [ ] Keyword extraction (TF-IDF or NLP)
- [ ] Sentiment analysis
- [ ] Reading time calculation
- [ ] Creates ProcessedContent entry

### Implementation Details
- Files to create/modify:
  - `apps/content/services.py`
- Use libraries: bleach, sklearn (TF-IDF), or spaCy
- Implementation:
  ```python
  class ContentProcessingService:
      def process_content(self, aggregated_content):
          # Clean HTML
          cleaned_body = bleach.clean(aggregated_content.content_body, strip=True)

          # Extract keywords
          keywords = self.extract_keywords(cleaned_body)

          # Sentiment analysis
          sentiment = self.analyze_sentiment(cleaned_body)

          # Create ProcessedContent
          processed = ProcessedContent.objects.create(
              aggregated_content=aggregated_content,
              cleaned_body=cleaned_body,
              keywords=keywords,
              sentiment_score=sentiment,
              # ...
          )

          return processed
  ```

### Testing Requirements
- Test HTML cleaning
- Test keyword extraction
- Test sentiment analysis
- Run: `pytest apps/content/tests/test_services.py::TestContentProcessingService`

---

## BUXMAX-067: Implement AIAvatarService

**Type**: API Integration
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-065

### Description
Create service for AI avatar interactions (generating responses, creating topics, participation logic).

### Acceptance Criteria
- [ ] AIAvatarService class created
- [ ] generate_response() method for forum replies
- [ ] create_topic() method for initiating discussions
- [ ] should_participate() logic for topic relevance
- [ ] Context building from topic history
- [ ] Persona-aware prompt generation
- [ ] Cooldown enforcement

### Implementation Details
- Files to create:
  - `apps/forum/services.py`
- Implementation:
  ```python
  class AIAvatarService:
      def generate_response(self, avatar, post):
          # Build context
          context = self.build_context(post.topic)

          # Build prompt with avatar persona
          prompt = self.build_response_prompt(avatar, post, context)

          # Generate response
          client = OpenAIClient(model=avatar.model_name)
          result = client.generate(
              prompt,
              temperature=avatar.temperature,
              max_tokens=avatar.max_tokens
          )

          # Create post
          response = ForumPost.objects.create(
              topic=post.topic,
              author=avatar,
              content=result['text']
          )

          # Update avatar metrics
          avatar.post_count += 1
          avatar.total_tokens_used += result['tokens_used']
          avatar.total_cost += result['cost']
          avatar.save()

          return response
  ```

### Testing Requirements
- Test response generation
- Test topic creation
- Test participation logic
- Run: `pytest apps/forum/tests/test_services.py::TestAIAvatarService`

---

## BUXMAX-068: Implement ModerationService

**Type**: API Integration
**Priority**: Critical
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-065

### Description
Create service for content moderation with multi-layer approach (keywords, AI analysis, decision logic).

### Acceptance Criteria
- [ ] ModerationService class created
- [ ] moderate() method with 3-layer approach
- [ ] Layer 1: Keyword/regex matching
- [ ] Layer 2: AI analysis for borderline content
- [ ] Layer 3: Decision logic
- [ ] Creates ModerationLog entries
- [ ] Updates content moderation_status
- [ ] Handles different content types (ForumPost, Comment)

### Implementation Details
- Reference: enhanced_plan.md Section 16.1.3 (lines 4310-4450)
- Files to create:
  - `apps/moderation/services.py`
- Implementation:
  ```python
  class ModerationService:
      def moderate(self, content_type, content_id):
          # Get content object
          content = self.get_content_object(content_type, content_id)

          # Layer 1: Keyword check
          keyword_result = self.check_keywords(content)
          if keyword_result['action'] in ['reject', 'approve']:
              return self.apply_decision(content, keyword_result)

          # Layer 2: AI analysis
          ai_result = self.ai_analyze(content)

          # Layer 3: Decision logic
          decision = self.make_decision(keyword_result, ai_result)

          # Apply and log
          return self.apply_decision(content, decision)
  ```

### Testing Requirements
- Test keyword matching
- Test AI analysis (with mock)
- Test decision logic
- Run: `pytest apps/moderation/tests/test_services.py::TestModerationService`

---

## BUXMAX-069: Create AI Client Tests

**Type**: Test
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-068

### Description
Write comprehensive tests for all AI clients with mocked API responses.

### Acceptance Criteria
- [ ] Test file created for AI clients
- [ ] Tests for OpenAIClient
- [ ] Tests for AnthropicClient
- [ ] Tests for rate limiting
- [ ] Tests for retry logic
- [ ] Tests for cost calculation
- [ ] All tests use mocked APIs
- [ ] All tests passing

### Implementation Details
- Reference: enhanced_plan.md Section 17.3.1 (lines 4801-4850)
- Files to create:
  - `apps/content/tests/test_ai_clients.py`
- Use @patch decorator to mock API calls

### Testing Requirements
- Run: `pytest apps/content/tests/test_ai_clients.py -v`
- Expected output: All tests pass, no real API calls made

---

## BUXMAX-070: Create Service Tests

**Type**: Test
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-069

### Description
Write tests for all service classes (AIGenerationService, ContentProcessingService, AIAvatarService, ModerationService).

### Acceptance Criteria
- [ ] Test files created for all services
- [ ] Tests for all service methods
- [ ] Tests with mocked dependencies
- [ ] Tests for error handling
- [ ] All tests passing
- [ ] Test coverage >80% for services

### Implementation Details
- Files to create:
  - `apps/content/tests/test_services.py`
  - `apps/forum/tests/test_services.py`
  - `apps/moderation/tests/test_services.py`

### Testing Requirements
- Run: `pytest apps/*/tests/test_services.py -v`
- Check coverage: `pytest --cov=apps --cov-report=html`
- Expected output: All tests pass, coverage >80%

---

# Phase 6: Frontend & Views (BUXMAX-071 to BUXMAX-085)

## BUXMAX-071: Create Base Templates

**Type**: Template
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-007

### Description
Create base HTML templates with navigation, footer, and common layout elements.

### Acceptance Criteria
- [ ] base.html template created
- [ ] Includes HTMX and Alpine.js
- [ ] Navigation component
- [ ] Footer component
- [ ] Message display area
- [ ] Block structure for content, CSS, JS
- [ ] Responsive design

### Implementation Details
- Reference: enhanced_plan.md Section 14.7.1 (lines 3731-3800)
- Files to create:
  - `templates/base.html`
  - `templates/components/navbar.html`
  - `templates/components/footer.html`
- Include HTMX: `<script src="{% static 'js/htmx.min.js' %}" defer></script>`

### Testing Requirements
- View in browser: Start server and visit homepage
- Test responsive design: Resize browser
- Expected behavior: Layout renders correctly

---

## BUXMAX-072: Implement URL Configuration

**Type**: Configuration
**Priority**: Critical
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-071

### Description
Create URL routing for all apps with proper namespacing.

### Acceptance Criteria
- [ ] Root urls.py configured
- [ ] URL patterns for content app
- [ ] URL patterns for forum app
- [ ] URL patterns for users app
- [ ] URL patterns for moderation app
- [ ] All URLs use namespaces
- [ ] Admin URLs included

### Implementation Details
- Reference: enhanced_plan.md Section 14.6 (lines 3524-3650)
- Files to create/modify:
  - `config/urls.py`
  - `apps/content/urls.py`
  - `apps/forum/urls.py`
  - `apps/users/urls.py`
  - `apps/moderation/urls.py`

### Testing Requirements
- Check URLs: `python manage.py show_urls` (if django-extensions installed)
- Test URL resolution: `python manage.py shell` then `reverse('content:article_list')`
- Expected output: All URLs resolve correctly

---

## BUXMAX-073: Implement Article Views

**Type**: View
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-072

### Description
Create views for displaying articles (list, detail) with pagination and filtering.

### Acceptance Criteria
- [ ] ArticleListView implemented
- [ ] ArticleDetailView implemented
- [ ] Pagination (20 items per page)
- [ ] Filtering by date, category
- [ ] Related articles display
- [ ] Comment display on detail page
- [ ] Views use class-based views

### Implementation Details
- Reference: enhanced_plan.md Section 14.6.4 (lines 3651-3730)
- Files to create/modify:
  - `apps/content/views.py`
- Implementation:
  ```python
  class ArticleListView(ListView):
      model = GeneratedArticle
      template_name = 'content/article_list.html'
      context_object_name = 'articles'
      paginate_by = 20

      def get_queryset(self):
          return GeneratedArticle.objects.filter(
              status='published'
          ).order_by('-published_at')
  ```

### Testing Requirements
- Test views: `pytest apps/content/tests/test_views.py`
- Manual test: Visit /content/articles/ in browser
- Expected behavior: Articles display correctly

---

## BUXMAX-074: Create Article Templates

**Type**: Template
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-073

### Description
Create HTML templates for article list and detail pages.

### Acceptance Criteria
- [ ] article_list.html template created
- [ ] article_detail.html template created
- [ ] Pagination controls
- [ ] Article cards with image, title, excerpt
- [ ] Detail page with full content
- [ ] Comment section
- [ ] Related articles sidebar
- [ ] Responsive design

### Implementation Details
- Files to create:
  - `apps/content/templates/content/article_list.html`
  - `apps/content/templates/content/article_detail.html`
- Use Django template tags for pagination, loops

### Testing Requirements
- View in browser
- Test pagination
- Test responsive design
- Expected behavior: Templates render correctly

---

## BUXMAX-075: Implement Forum Views

**Type**: View
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-072

### Description
Create views for forum (home, category, topic, post creation/editing).

### Acceptance Criteria
- [ ] ForumHomeView (list categories)
- [ ] CategoryDetailView (list topics)
- [ ] TopicDetailView (list posts)
- [ ] TopicCreateView
- [ ] PostCreateView (HTMX endpoint)
- [ ] PostUpdateView
- [ ] PostDeleteView
- [ ] Proper permissions (login required for posting)

### Implementation Details
- Reference: enhanced_plan.md Section 14.6.3 (lines 3600-3650)
- Files to create/modify:
  - `apps/forum/views.py`
- Use LoginRequiredMixin for protected views

### Testing Requirements
- Test all views: `pytest apps/forum/tests/test_views.py`
- Manual test: Navigate forum in browser
- Expected behavior: All forum functions work

---

## BUXMAX-076: Create Forum Templates

**Type**: Template
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-075

### Description
Create HTML templates for all forum pages with HTMX for dynamic interactions.

### Acceptance Criteria
- [ ] forum_home.html (category list)
- [ ] category_detail.html (topic list)
- [ ] topic_detail.html (post list + reply form)
- [ ] topic_form.html (create topic)
- [ ] post_form.html (HTMX partial)
- [ ] HTMX for posting without page reload
- [ ] AI avatar posts visually distinguished
- [ ] Responsive design

### Implementation Details
- Reference: enhanced_plan.md Section 14.7.2 (lines 3801-3900)
- Files to create:
  - `apps/forum/templates/forum/*.html`
- HTMX example:
  ```html
  <form hx-post="{% url 'forum:post_create' topic.id %}"
        hx-target="#posts-container"
        hx-swap="beforeend">
  ```

### Testing Requirements
- Test HTMX interactions
- Test AI post styling
- Expected behavior: Dynamic posting works

---

## BUXMAX-077: Implement Comment System

**Type**: View
**Priority**: Medium
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-074

### Description
Implement comment functionality for articles with HTMX for dynamic submission.

### Acceptance Criteria
- [ ] AddCommentView (HTMX endpoint)
- [ ] Comment form template
- [ ] Comment list template
- [ ] Threaded comments support
- [ ] Moderation integration
- [ ] Login required for commenting
- [ ] HTMX for submission without reload

### Implementation Details
- Files to create/modify:
  - `apps/content/views.py`
  - `apps/content/forms.py`
  - `apps/content/templates/content/comment_*.html`

### Testing Requirements
- Test comment submission
- Test HTMX behavior
- Test moderation trigger
- Run: `pytest apps/content/tests/test_views.py::TestAddCommentView`

---

## BUXMAX-078: Implement User Authentication Views

**Type**: View
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-072

### Description
Implement user registration, login, logout, and profile views.

### Acceptance Criteria
- [ ] Registration view and form
- [ ] Login view (use Django auth)
- [ ] Logout view
- [ ] Profile view
- [ ] Profile edit view
- [ ] Password change view
- [ ] Email verification (optional)

### Implementation Details
- Files to create/modify:
  - `apps/users/views.py`
  - `apps/users/forms.py`
- Use Django's built-in auth views where possible

### Testing Requirements
- Test registration flow
- Test login/logout
- Test profile editing
- Run: `pytest apps/users/tests/test_views.py`

---

## BUXMAX-079: Create User Templates

**Type**: Template
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-078

### Description
Create templates for user authentication and profile pages.

### Acceptance Criteria
- [ ] registration.html
- [ ] login.html
- [ ] profile.html
- [ ] profile_edit.html
- [ ] password_change.html
- [ ] Consistent styling with base template
- [ ] Form validation display

### Implementation Details
- Files to create:
  - `apps/users/templates/users/*.html`
  - `apps/users/templates/registration/*.html`

### Testing Requirements
- View all templates in browser
- Test form validation display
- Expected behavior: All forms work correctly

---

## BUXMAX-080: Implement Newsletter Subscription

**Type**: View
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-078

### Description
Implement newsletter subscription/unsubscription functionality.

### Acceptance Criteria
- [ ] NewsletterSubscribeView
- [ ] NewsletterUnsubscribeView
- [ ] Email confirmation (double opt-in)
- [ ] Subscription preferences
- [ ] HTMX for inline subscription

### Implementation Details
- Files to create/modify:
  - `apps/content/views.py`
  - `apps/content/forms.py`

### Testing Requirements
- Test subscription flow
- Test confirmation email
- Run: `pytest apps/content/tests/test_views.py::TestNewsletterSubscribeView`

---

## BUXMAX-081: Implement RSS Feed

**Type**: View
**Priority**: Low
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-073

### Description
Implement RSS feed for published articles.

### Acceptance Criteria
- [ ] ContentRSSFeed class created
- [ ] Includes latest 50 articles
- [ ] Proper RSS 2.0 format
- [ ] Feed accessible at /content/feed/
- [ ] Feed linked in HTML head

### Implementation Details
- Files to create/modify:
  - `apps/content/feeds.py`
  - `apps/content/urls.py`
- Use Django's syndication framework

### Testing Requirements
- Test feed: Visit /content/feed/ in browser
- Validate RSS: Use RSS validator
- Expected output: Valid RSS feed

---

## BUXMAX-082: Add Static Assets

**Type**: Configuration
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-071

### Description
Add CSS, JavaScript, and image assets for the frontend.

### Acceptance Criteria
- [ ] CSS files created (base.css, components.css)
- [ ] HTMX library added
- [ ] Alpine.js library added
- [ ] Custom JavaScript (app.js)
- [ ] Favicon and logo images
- [ ] Static files collected

### Implementation Details
- Files to create:
  - `static/css/base.css`
  - `static/js/htmx.min.js`
  - `static/js/alpine.min.js`
  - `static/js/app.js`
  - `static/images/logo.png`
- Run: `python manage.py collectstatic`

### Testing Requirements
- Verify static files load in browser
- Check browser console for errors
- Expected behavior: All assets load correctly

---

## BUXMAX-083: Implement Search Functionality

**Type**: View
**Priority**: Low
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-073

### Description
Implement search functionality for articles and forum posts.

### Acceptance Criteria
- [ ] SearchView implemented
- [ ] Searches articles and forum posts
- [ ] Full-text search using PostgreSQL
- [ ] Search results page
- [ ] Search form in navbar
- [ ] Pagination for results
- [ ] Highlighting of search terms

### Implementation Details
- Files to create/modify:
  - `apps/core/views.py`
  - `apps/core/templates/core/search_results.html`
- Use Django's SearchVector for PostgreSQL full-text search

### Testing Requirements
- Test search with various queries
- Test result relevance
- Run: `pytest apps/core/tests/test_views.py::TestSearchView`

---

## BUXMAX-084: Create View Tests

**Type**: Test
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-083

### Description
Write comprehensive tests for all views including GET/POST requests, permissions, and edge cases.

### Acceptance Criteria
- [ ] Test files for all view modules
- [ ] Tests for successful requests
- [ ] Tests for permission checks
- [ ] Tests for form validation
- [ ] Tests for HTMX endpoints
- [ ] All tests passing
- [ ] Test coverage >80% for views

### Implementation Details
- Files to create:
  - `apps/content/tests/test_views.py`
  - `apps/forum/tests/test_views.py`
  - `apps/users/tests/test_views.py`
- Use Django's test client

### Testing Requirements
- Run: `pytest apps/*/tests/test_views.py -v`
- Check coverage: `pytest --cov=apps --cov-report=html`
- Expected output: All tests pass, coverage >80%

---

## BUXMAX-085: Create Frontend Documentation

**Type**: Documentation
**Priority**: Low
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-084

### Description
Create documentation for frontend architecture, templates, and HTMX usage.

### Acceptance Criteria
- [ ] Documentation file created
- [ ] Template hierarchy explained
- [ ] HTMX patterns documented
- [ ] Component usage guide
- [ ] Styling guidelines
- [ ] JavaScript integration

### Implementation Details
- Files to create:
  - `docs/frontend_guide.md`

### Testing Requirements
- Review documentation for completeness
- Expected output: Clear, comprehensive documentation

---

# Phase 7: Moderation System (BUXMAX-086 to BUXMAX-095)

## BUXMAX-086: Create Moderation Rules Interface

**Type**: View
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-023

### Description
Create admin interface for managing moderation rules (keywords, regex patterns).

### Acceptance Criteria
- [ ] Enhanced admin for ModerationRule
- [ ] Bulk actions (activate/deactivate)
- [ ] Rule testing interface
- [ ] Import/export rules
- [ ] Rule effectiveness metrics
- [ ] Search and filtering

### Implementation Details
- Files to modify:
  - `apps/moderation/admin.py`
- Add custom admin actions and views

### Testing Requirements
- Test rule creation in admin
- Test bulk actions
- Expected behavior: Rules manageable via admin

---

## BUXMAX-087: Create Moderation Queue Interface

**Type**: View
**Priority**: Critical
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-086

### Description
Create interface for human moderators to review flagged content.

### Acceptance Criteria
- [ ] Moderation queue view (list flagged content)
- [ ] Content review view (approve/reject/edit)
- [ ] Filtering by content type, severity
- [ ] Bulk moderation actions
- [ ] Moderation history display
- [ ] Staff-only access

### Implementation Details
- Files to create:
  - `apps/moderation/views.py`
  - `apps/moderation/templates/moderation/*.html`
- Use StaffRequiredMixin for permissions

### Testing Requirements
- Test queue display
- Test moderation actions
- Test permissions
- Run: `pytest apps/moderation/tests/test_views.py`

---

## BUXMAX-088: Implement User Reporting

**Type**: View
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-087

### Description
Implement functionality for users to report inappropriate content.

### Acceptance Criteria
- [ ] Report button on posts/comments
- [ ] Report form with reason selection
- [ ] Creates ModerationLog with action='flagged_user'
- [ ] HTMX for inline reporting
- [ ] Prevents duplicate reports
- [ ] Notification to moderators

### Implementation Details
- Files to create/modify:
  - `apps/moderation/views.py`
  - `apps/moderation/forms.py`
  - Templates with report buttons

### Testing Requirements
- Test report submission
- Test duplicate prevention
- Run: `pytest apps/moderation/tests/test_views.py::TestReportContentView`

---

## BUXMAX-089: Implement Moderation Signals

**Type**: Configuration
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-068

### Description
Set up Django signals to automatically trigger moderation on content creation.

### Acceptance Criteria
- [ ] Signal handler for ForumPost creation
- [ ] Signal handler for Comment creation
- [ ] Dispatches moderate_content task
- [ ] Handles signal errors gracefully
- [ ] Logging for signal execution

### Implementation Details
- Files to create:
  - `apps/moderation/signals.py`
- Register signals in apps.py:
  ```python
  @receiver(post_save, sender=ForumPost)
  def trigger_moderation(sender, instance, created, **kwargs):
      if created:
          moderate_content.delay('forum_post', instance.id)
  ```

### Testing Requirements
- Test signal triggers on creation
- Test task dispatch
- Run: `pytest apps/moderation/tests/test_signals.py`

---

## BUXMAX-090: Create Moderation Dashboard

**Type**: View
**Priority**: Medium
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-087

### Description
Create dashboard for moderation statistics and insights.

### Acceptance Criteria
- [ ] Dashboard view with metrics
- [ ] Charts for moderation actions over time
- [ ] Top flagged users/content
- [ ] Rule effectiveness statistics
- [ ] AI vs human moderation comparison
- [ ] Export functionality

### Implementation Details
- Files to create:
  - `apps/moderation/views.py` (DashboardView)
  - `apps/moderation/templates/moderation/dashboard.html`
- Use Chart.js or similar for visualizations

### Testing Requirements
- Test dashboard display
- Test metrics calculation
- Expected behavior: Dashboard shows accurate stats

---

## BUXMAX-091: Implement Content Appeals

**Type**: View
**Priority**: Low
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-087

### Description
Allow users to appeal moderation decisions on their content.

### Acceptance Criteria
- [ ] Appeal form for rejected content
- [ ] Appeal review interface for moderators
- [ ] Appeal status tracking
- [ ] Email notifications for appeal decisions
- [ ] Appeal history

### Implementation Details
- Files to create/modify:
  - `apps/moderation/models.py` (Appeal model)
  - `apps/moderation/views.py`
  - Templates for appeal forms

### Testing Requirements
- Test appeal submission
- Test appeal review
- Run: `pytest apps/moderation/tests/test_views.py::TestAppealView`

---

## BUXMAX-092: Add Moderation Metrics

**Type**: Configuration
**Priority**: Low
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-090

### Description
Add comprehensive metrics tracking for moderation system performance.

### Acceptance Criteria
- [ ] Track moderation response time
- [ ] Track false positive/negative rates
- [ ] Track moderator performance
- [ ] Track rule effectiveness
- [ ] Metrics stored in database
- [ ] Metrics displayed in dashboard

### Implementation Details
- Files to modify:
  - `apps/moderation/models.py` (add metrics fields)
  - `apps/moderation/services.py` (track metrics)

### Testing Requirements
- Test metrics calculation
- Test metrics display
- Expected behavior: Accurate metrics tracking

---

## BUXMAX-093: Create Moderation Tests

**Type**: Test
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-092

### Description
Write comprehensive tests for moderation system including rules, queue, and signals.

### Acceptance Criteria
- [ ] Tests for ModerationService
- [ ] Tests for moderation views
- [ ] Tests for signals
- [ ] Tests for rule matching
- [ ] Tests for AI moderation (mocked)
- [ ] All tests passing
- [ ] Test coverage >80%

### Implementation Details
- Files to create:
  - `apps/moderation/tests/test_services.py`
  - `apps/moderation/tests/test_views.py`
  - `apps/moderation/tests/test_signals.py`

### Testing Requirements
- Run: `pytest apps/moderation/tests/ -v`
- Check coverage: `pytest --cov=apps.moderation --cov-report=html`
- Expected output: All tests pass, coverage >80%

---

## BUXMAX-094: Implement Moderation API (Optional)

**Type**: API Integration
**Priority**: Low
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-093

### Description
Create REST API endpoints for moderation system (for mobile app or external tools).

### Acceptance Criteria
- [ ] API endpoints for moderation queue
- [ ] API endpoints for moderation actions
- [ ] API authentication
- [ ] API documentation
- [ ] Rate limiting

### Implementation Details
- Use Django REST Framework
- Files to create:
  - `apps/moderation/api/serializers.py`
  - `apps/moderation/api/views.py`
  - `apps/moderation/api/urls.py`

### Testing Requirements
- Test API endpoints
- Test authentication
- Run: `pytest apps/moderation/tests/test_api.py`

---

## BUXMAX-095: Create Moderation Documentation

**Type**: Documentation
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-094

### Description
Create comprehensive documentation for moderation system including guidelines and procedures.

### Acceptance Criteria
- [ ] Moderation guidelines document
- [ ] Rule creation guide
- [ ] Queue management procedures
- [ ] Appeal handling process
- [ ] Troubleshooting guide
- [ ] Best practices

### Implementation Details
- Files to create:
  - `docs/moderation_guide.md`
  - `docs/moderation_guidelines.md`

### Testing Requirements
- Review documentation for completeness
- Expected output: Clear, comprehensive documentation

---

# Phase 8: Testing (BUXMAX-096 to BUXMAX-110)

## BUXMAX-096: Configure Pytest

**Type**: Test
**Priority**: Critical
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-027

### Description
Configure pytest with Django integration, coverage reporting, and test database settings.

### Acceptance Criteria
- [ ] pytest.ini created with configuration
- [ ] pytest-django installed and configured
- [ ] Coverage configuration
- [ ] Test database settings
- [ ] Parallel test execution configured
- [ ] Fixtures auto-discovery

### Implementation Details
- Reference: enhanced_plan.md Section 17.2.1 (lines 4651-4700)
- Files to create:
  - `pytest.ini`
  - `.coveragerc`
- Configuration:
  ```ini
  [pytest]
  DJANGO_SETTINGS_MODULE = config.settings.testing
  python_files = test_*.py
  python_classes = Test*
  python_functions = test_*
  addopts = --cov=apps --cov-report=html --reuse-db
  ```

### Testing Requirements
- Run pytest: `pytest`
- Expected output: Tests discovered and run

---

## BUXMAX-097: Create Testing Settings

**Type**: Configuration
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-096

### Description
Create dedicated settings file for testing with optimizations for test speed.

### Acceptance Criteria
- [ ] config/settings/testing.py created
- [ ] Inherits from base settings
- [ ] In-memory database or fast test database
- [ ] Disabled unnecessary middleware
- [ ] Simplified password hashers
- [ ] Disabled migrations (--nomigrations)

### Implementation Details
- Files to create:
  - `config/settings/testing.py`
- Key settings:
  ```python
  from .base import *

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': ':memory:',
      }
  }

  PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
  ```

### Testing Requirements
- Run tests with testing settings
- Verify faster execution
- Expected output: Tests run quickly

---

## BUXMAX-098: Write Integration Tests

**Type**: Test
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-097

### Description
Write integration tests that test multiple components working together (e.g., scraping → processing → generation).

### Acceptance Criteria
- [ ] Integration test file created
- [ ] Test scraping to database flow
- [ ] Test content processing pipeline
- [ ] Test AI generation workflow
- [ ] Test forum interaction flow
- [ ] Test moderation workflow
- [ ] All tests passing

### Implementation Details
- Files to create:
  - `tests/integration/test_content_pipeline.py`
  - `tests/integration/test_forum_workflow.py`
  - `tests/integration/test_moderation_workflow.py`
- Use @pytest.mark.integration decorator

### Testing Requirements
- Run: `pytest tests/integration/ -v`
- Expected output: All integration tests pass

---

## BUXMAX-099: Write End-to-End Tests

**Type**: Test
**Priority**: Medium
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-098

### Description
Write end-to-end tests using Selenium or Playwright to test user workflows in browser.

### Acceptance Criteria
- [ ] E2E test framework configured (Playwright)
- [ ] Test user registration and login
- [ ] Test article browsing
- [ ] Test forum posting
- [ ] Test comment submission
- [ ] Test newsletter subscription
- [ ] All tests passing

### Implementation Details
- Files to create:
  - `tests/e2e/test_user_workflows.py`
  - `tests/e2e/conftest.py`
- Use Playwright for browser automation

### Testing Requirements
- Run: `pytest tests/e2e/ -v`
- Expected output: All E2E tests pass

---

## BUXMAX-100: Create Performance Tests

**Type**: Test
**Priority**: Low
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-098

### Description
Write performance tests to ensure system meets performance requirements.

### Acceptance Criteria
- [ ] Performance test file created
- [ ] Test database query performance
- [ ] Test API response times
- [ ] Test page load times
- [ ] Test concurrent user handling
- [ ] Performance benchmarks documented

### Implementation Details
- Files to create:
  - `tests/performance/test_query_performance.py`
  - `tests/performance/test_api_performance.py`
- Use pytest-benchmark or locust

### Testing Requirements
- Run: `pytest tests/performance/ -v`
- Expected output: All performance tests pass

---

## BUXMAX-101: Create Load Tests

**Type**: Test
**Priority**: Low
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-100

### Description
Create load tests to verify system behavior under high traffic.

### Acceptance Criteria
- [ ] Load test scripts created
- [ ] Test concurrent scraping tasks
- [ ] Test concurrent API requests
- [ ] Test concurrent user sessions
- [ ] Load test results documented
- [ ] System remains stable under load

### Implementation Details
- Files to create:
  - `tests/load/locustfile.py`
- Use Locust for load testing
- Test scenarios:
  - 100 concurrent users browsing
  - 50 concurrent scraping tasks
  - 20 concurrent AI generation tasks

### Testing Requirements
- Run: `locust -f tests/load/locustfile.py`
- Expected output: System handles load without errors

---

## BUXMAX-102: Implement Test Data Fixtures

**Type**: Test
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-027

### Description
Create comprehensive test data fixtures for consistent testing across all test suites.

### Acceptance Criteria
- [ ] Fixture files created for all models
- [ ] JSON fixtures for initial data
- [ ] Factory fixtures for dynamic data
- [ ] Fixtures for different scenarios (empty, populated, edge cases)
- [ ] Fixtures documented

### Implementation Details
- Files to create:
  - `apps/*/fixtures/*.json`
  - `tests/fixtures/conftest.py`
- Use Django's dumpdata/loaddata

### Testing Requirements
- Load fixtures: `python manage.py loaddata fixture_name`
- Verify data loaded correctly
- Expected output: Fixtures load without errors

---

## BUXMAX-103: Create Test Utilities

**Type**: Test
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-096

### Description
Create utility functions and helpers for testing (mock factories, assertion helpers, test decorators).

### Acceptance Criteria
- [ ] Test utilities module created
- [ ] Mock factories for external services
- [ ] Custom assertion helpers
- [ ] Test decorators (skip_if, requires_api_key)
- [ ] Utilities documented

### Implementation Details
- Files to create:
  - `tests/utils.py`
- Example utilities:
  ```python
  def create_mock_openai_response(text, tokens=100):
      """Create mock OpenAI API response."""
      pass

  def assert_moderation_logged(content, action):
      """Assert moderation log created."""
      pass
  ```

### Testing Requirements
- Test utilities themselves
- Use in other tests
- Expected output: Utilities work correctly

---

## BUXMAX-104: Implement Continuous Testing

**Type**: Configuration
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-096

### Description
Set up continuous testing with pytest-watch for development.

### Acceptance Criteria
- [ ] pytest-watch configured
- [ ] Watches for file changes
- [ ] Runs relevant tests automatically
- [ ] Clear output formatting
- [ ] Documentation for usage

### Implementation Details
- Install: `pip install pytest-watch`
- Usage: `ptw -- -v`
- Add to development documentation

### Testing Requirements
- Run pytest-watch
- Make code change
- Verify tests run automatically
- Expected behavior: Tests run on file save

---

## BUXMAX-105: Create Test Coverage Reports

**Type**: Test
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-096

### Description
Configure comprehensive test coverage reporting with HTML and terminal output.

### Acceptance Criteria
- [ ] Coverage configuration complete
- [ ] HTML coverage reports generated
- [ ] Terminal coverage summary
- [ ] Coverage badges (optional)
- [ ] Coverage thresholds enforced (>80%)
- [ ] Uncovered lines highlighted

### Implementation Details
- Files to modify:
  - `pytest.ini`
  - `.coveragerc`
- Configuration:
  ```ini
  [coverage:run]
  source = apps
  omit = */migrations/*, */tests/*

  [coverage:report]
  fail_under = 80
  ```

### Testing Requirements
- Run: `pytest --cov=apps --cov-report=html --cov-report=term`
- Open: `htmlcov/index.html`
- Expected output: Coverage >80%, clear reports

---

## BUXMAX-106: Write Security Tests

**Type**: Test
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-098

### Description
Write tests to verify security measures (authentication, authorization, input validation, XSS, CSRF).

### Acceptance Criteria
- [ ] Test authentication requirements
- [ ] Test authorization (permissions)
- [ ] Test CSRF protection
- [ ] Test XSS prevention
- [ ] Test SQL injection prevention
- [ ] Test rate limiting
- [ ] All security tests passing

### Implementation Details
- Files to create:
  - `tests/security/test_authentication.py`
  - `tests/security/test_authorization.py`
  - `tests/security/test_input_validation.py`
- Test scenarios:
  - Unauthenticated access to protected views
  - Unauthorized access to other users' data
  - Malicious input handling

### Testing Requirements
- Run: `pytest tests/security/ -v`
- Expected output: All security tests pass

---

## BUXMAX-107: Create API Tests (if applicable)

**Type**: Test
**Priority**: Low
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-094

### Description
Write tests for REST API endpoints if API is implemented.

### Acceptance Criteria
- [ ] Test all API endpoints
- [ ] Test authentication
- [ ] Test serialization
- [ ] Test filtering and pagination
- [ ] Test error responses
- [ ] Test rate limiting
- [ ] All API tests passing

### Implementation Details
- Files to create:
  - `apps/*/tests/test_api.py`
- Use Django REST Framework's APIClient

### Testing Requirements
- Run: `pytest apps/*/tests/test_api.py -v`
- Expected output: All API tests pass

---

## BUXMAX-108: Implement Test Documentation

**Type**: Documentation
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-107

### Description
Create comprehensive documentation for testing strategy, running tests, and writing new tests.

### Acceptance Criteria
- [ ] Testing guide created
- [ ] How to run tests
- [ ] How to write tests
- [ ] Testing best practices
- [ ] Coverage requirements
- [ ] CI/CD integration guide

### Implementation Details
- Files to create:
  - `docs/testing_guide.md`
- Sections:
  - Running tests
  - Writing unit tests
  - Writing integration tests
  - Using factories and fixtures
  - Mocking external services
  - Coverage requirements

### Testing Requirements
- Review documentation
- Follow guide to write a test
- Expected output: Clear, comprehensive guide

---

## BUXMAX-109: Create Test Data Seeding Script

**Type**: Configuration
**Priority**: Low
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-102

### Description
Create management command to seed database with test data for development and testing.

### Acceptance Criteria
- [ ] Management command created
- [ ] Seeds all model types
- [ ] Configurable data volume
- [ ] Idempotent (can run multiple times)
- [ ] Progress output
- [ ] Documentation

### Implementation Details
- Files to create:
  - `apps/core/management/commands/seed_data.py`
- Usage: `python manage.py seed_data --sources=10 --articles=50`

### Testing Requirements
- Run command
- Verify data created
- Run again, verify no duplicates
- Expected output: Database seeded successfully

---

## BUXMAX-110: Run Full Test Suite

**Type**: Test
**Priority**: Critical
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-109

### Description
Run complete test suite and verify all tests pass with adequate coverage.

### Acceptance Criteria
- [ ] All unit tests passing
- [ ] All integration tests passing
- [ ] All E2E tests passing (if implemented)
- [ ] Test coverage >80%
- [ ] No test warnings or errors
- [ ] Test execution time reasonable (<5 min for unit tests)

### Implementation Details
- Commands to run:
  ```bash
  pytest -v --cov=apps --cov-report=html --cov-report=term
  pytest tests/integration/ -v
  pytest tests/e2e/ -v
  ```

### Testing Requirements
- Run full suite
- Review coverage report
- Fix any failing tests
- Expected output: All tests pass, coverage >80%

---

# Phase 9: Deployment (BUXMAX-111 to BUXMAX-120)

## BUXMAX-111: Create Docker Configuration

**Type**: Configuration
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-006

### Description
Create production-ready Docker configuration with multi-stage builds and optimization.

### Acceptance Criteria
- [ ] Dockerfile created with multi-stage build
- [ ] docker-compose.yml for development
- [ ] docker-compose.prod.yml for production
- [ ] All services defined (web, worker, beat, db, redis)
- [ ] Volume mounts configured
- [ ] Environment variables configured
- [ ] Health checks implemented

### Implementation Details
- Reference: enhanced_plan.md Section 15.4 (lines 4251-4309)
- Files to create:
  - `Dockerfile`
  - `docker-compose.yml`
  - `docker-compose.prod.yml`
  - `.dockerignore`

### Testing Requirements
- Build: `docker-compose build`
- Run: `docker-compose up`
- Verify all services start
- Expected output: All containers running

---

## BUXMAX-112: Configure Production Server

**Type**: Configuration
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-111

### Description
Configure Gunicorn for production with appropriate worker settings and logging.

### Acceptance Criteria
- [ ] Gunicorn configuration file created
- [ ] Worker count optimized (2 * CPU + 1)
- [ ] Timeout settings configured
- [ ] Access and error logging
- [ ] Graceful shutdown handling
- [ ] Static file serving with WhiteNoise

### Implementation Details
- Files to create:
  - `gunicorn.conf.py`
- Configuration:
  ```python
  bind = "0.0.0.0:8000"
  workers = 4
  worker_class = "sync"
  timeout = 120
  accesslog = "-"
  errorlog = "-"
  ```

### Testing Requirements
- Run: `gunicorn config.wsgi:application -c gunicorn.conf.py`
- Test with load
- Expected output: Server handles requests efficiently

---

## BUXMAX-113: Set Up CI/CD Pipeline

**Type**: Configuration
**Priority**: High
**Complexity**: Large (1-2 days)
**Dependencies**: BUXMAX-110

### Description
Create CI/CD pipeline using GitHub Actions for automated testing and deployment.

### Acceptance Criteria
- [ ] GitHub Actions workflow created
- [ ] Runs tests on every push
- [ ] Runs linting (black, flake8)
- [ ] Builds Docker image
- [ ] Deploys to staging on merge to develop
- [ ] Deploys to production on merge to main
- [ ] Notifications on failure

### Implementation Details
- Files to create:
  - `.github/workflows/ci.yml`
  - `.github/workflows/deploy.yml`
- Workflow steps:
  - Checkout code
  - Set up Python
  - Install dependencies
  - Run tests
  - Build Docker image
  - Push to registry
  - Deploy to server

### Testing Requirements
- Push to repository
- Verify workflow runs
- Check test results
- Expected output: Workflow completes successfully

---

## BUXMAX-114: Configure Monitoring

**Type**: Configuration
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-112

### Description
Set up application monitoring with Sentry for error tracking and performance monitoring.

### Acceptance Criteria
- [ ] Sentry SDK integrated
- [ ] Error tracking configured
- [ ] Performance monitoring enabled
- [ ] Custom tags and context
- [ ] Release tracking
- [ ] User feedback integration

### Implementation Details
- Files to modify:
  - `config/settings/production.py`
- Configuration:
  ```python
  import sentry_sdk
  from sentry_sdk.integrations.django import DjangoIntegration

  sentry_sdk.init(
      dsn=os.getenv('SENTRY_DSN'),
      integrations=[DjangoIntegration()],
      traces_sample_rate=0.1,
  )
  ```

### Testing Requirements
- Trigger test error
- Verify error appears in Sentry
- Expected output: Errors tracked in Sentry

---

## BUXMAX-115: Set Up Logging

**Type**: Configuration
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-112

### Description
Configure comprehensive logging for production with log rotation and aggregation.

### Acceptance Criteria
- [ ] Logging configuration in settings
- [ ] Different log levels for different modules
- [ ] Log rotation configured
- [ ] Structured logging (JSON format)
- [ ] Log aggregation (optional: ELK stack)
- [ ] Sensitive data filtering

### Implementation Details
- Files to modify:
  - `config/settings/production.py`
- Use Python's logging module
- Configure handlers for file, console, and external services

### Testing Requirements
- Generate logs
- Verify log files created
- Check log rotation
- Expected output: Logs properly formatted and rotated

---

## BUXMAX-116: Configure Backup Strategy

**Type**: Configuration
**Priority**: High
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-112

### Description
Implement automated backup strategy for database and media files.

### Acceptance Criteria
- [ ] Database backup script created
- [ ] Media files backup configured
- [ ] Automated daily backups
- [ ] Backup retention policy (30 days)
- [ ] Backup verification
- [ ] Restore procedure documented

### Implementation Details
- Files to create:
  - `scripts/backup_database.sh`
  - `scripts/backup_media.sh`
- Use pg_dump for PostgreSQL
- Store backups in S3 or similar

### Testing Requirements
- Run backup script
- Verify backup created
- Test restore procedure
- Expected output: Backups created and restorable

---

## BUXMAX-117: Set Up SSL/TLS

**Type**: Configuration
**Priority**: Critical
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-112

### Description
Configure SSL/TLS certificates for HTTPS using Let's Encrypt.

### Acceptance Criteria
- [ ] SSL certificate obtained
- [ ] HTTPS configured
- [ ] HTTP to HTTPS redirect
- [ ] Certificate auto-renewal
- [ ] Security headers configured
- [ ] SSL test passes (A+ rating)

### Implementation Details
- Use Certbot for Let's Encrypt
- Configure nginx or load balancer
- Update Django settings:
  ```python
  SECURE_SSL_REDIRECT = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True
  ```

### Testing Requirements
- Visit site via HTTPS
- Test SSL: https://www.ssllabs.com/ssltest/
- Expected output: A+ SSL rating

---

## BUXMAX-118: Configure CDN (Optional)

**Type**: Configuration
**Priority**: Low
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-117

### Description
Set up CDN for static assets and media files to improve performance.

### Acceptance Criteria
- [ ] CDN configured (CloudFlare or similar)
- [ ] Static files served via CDN
- [ ] Media files served via CDN
- [ ] Cache headers configured
- [ ] CDN purge on deployment

### Implementation Details
- Configure CloudFlare or AWS CloudFront
- Update Django settings:
  ```python
  STATIC_URL = 'https://cdn.example.com/static/'
  MEDIA_URL = 'https://cdn.example.com/media/'
  ```

### Testing Requirements
- Verify assets load from CDN
- Check cache headers
- Expected output: Assets served via CDN

---

## BUXMAX-119: Create Deployment Documentation

**Type**: Documentation
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-118

### Description
Create comprehensive deployment documentation including setup, deployment, and rollback procedures.

### Acceptance Criteria
- [ ] Deployment guide created
- [ ] Server setup instructions
- [ ] Deployment procedure
- [ ] Rollback procedure
- [ ] Troubleshooting guide
- [ ] Environment variables reference

### Implementation Details
- Files to create:
  - `docs/deployment_guide.md`
- Sections:
  - Prerequisites
  - Initial server setup
  - Deployment steps
  - Post-deployment checks
  - Rollback procedure
  - Common issues and solutions

### Testing Requirements
- Follow guide to deploy
- Verify all steps work
- Expected output: Successful deployment following guide

---

## BUXMAX-120: Perform Production Deployment

**Type**: Setup
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-119

### Description
Deploy application to production environment and verify all systems operational.

### Acceptance Criteria
- [ ] Application deployed to production
- [ ] Database migrated
- [ ] Static files collected and served
- [ ] All services running (web, worker, beat)
- [ ] SSL certificate active
- [ ] Monitoring active
- [ ] Backups configured
- [ ] Health checks passing

### Implementation Details
- Follow deployment guide
- Steps:
  1. Provision server
  2. Install dependencies
  3. Deploy code
  4. Run migrations
  5. Collect static files
  6. Start services
  7. Verify functionality

### Testing Requirements
- Access production site
- Test all major features
- Check monitoring dashboards
- Verify backups running
- Expected output: Production site fully operational

---

# Phase 10: Launch & Iteration (BUXMAX-121 to BUXMAX-130)

## BUXMAX-121: Seed Initial Sources

**Type**: Setup
**Priority**: Critical
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-120

### Description
Research and add initial set of high-quality frugal living sources to the database.

### Acceptance Criteria
- [ ] 50+ sources added
- [ ] Sources cover various frugal living topics
- [ ] Sources verified for quality and relevance
- [ ] Sources configured with appropriate scrape frequency
- [ ] Sources categorized by type (blog, RSS, news)
- [ ] Target regions set (US, CA)

### Implementation Details
- Research frugal living blogs, news sites, forums
- Add via Django admin or management command
- Verify robots.txt compliance
- Test scraping for each source

### Testing Requirements
- Verify sources added
- Test scraping a few sources
- Expected output: 50+ quality sources in database

---

## BUXMAX-122: Run Initial Scraping

**Type**: Setup
**Priority**: Critical
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-121

### Description
Execute initial scraping run to populate database with content.

### Acceptance Criteria
- [ ] Scraping tasks dispatched for all sources
- [ ] Content successfully aggregated
- [ ] No major errors
- [ ] Content processed
- [ ] Metrics tracked

### Implementation Details
- Trigger: `python manage.py shell` then:
  ```python
  from apps.aggregation.tasks import scrape_due_sources
  scrape_due_sources.delay()
  ```
- Monitor Flower dashboard
- Check logs for errors

### Testing Requirements
- Verify content in database
- Check AggregatedContent count
- Review error logs
- Expected output: 100+ content items aggregated

---

## BUXMAX-123: Generate Initial AI Content

**Type**: Setup
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-122

### Description
Generate initial set of AI articles from aggregated content.

### Acceptance Criteria
- [ ] 10+ articles generated
- [ ] Articles reviewed for quality
- [ ] Articles published
- [ ] Cost tracked
- [ ] No generation errors

### Implementation Details
- Trigger: `python manage.py shell` then:
  ```python
  from apps.content.tasks import generate_daily_summary
  generate_daily_summary.delay()
  ```
- Review generated articles in admin
- Publish quality articles

### Testing Requirements
- Verify articles created
- Review article quality
- Check generation costs
- Expected output: 10+ quality articles published

---

## BUXMAX-124: Create Initial Forum Structure

**Type**: Setup
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-120

### Description
Create initial forum categories and seed with topics.

### Acceptance Criteria
- [ ] 5-10 forum categories created
- [ ] Categories cover main frugal living topics
- [ ] 2-3 seed topics per category
- [ ] Topics have initial posts
- [ ] Categories ordered logically

### Implementation Details
- Create via Django admin
- Categories:
  - Budgeting & Saving
  - Frugal Food & Cooking
  - DIY & Repairs
  - Thrifting & Second-Hand
  - Energy Saving
  - Transportation
  - General Discussion
- Create seed topics with engaging questions

### Testing Requirements
- Verify categories visible
- Test topic creation
- Expected output: Active forum structure

---

## BUXMAX-125: Activate AI Avatars

**Type**: Setup
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-124

### Description
Create and activate AI avatars to participate in forum discussions.

### Acceptance Criteria
- [ ] 2-3 AI avatars created
- [ ] Avatars have distinct personas
- [ ] Avatars configured with appropriate settings
- [ ] Avatars set to active
- [ ] Initial avatar posts created

### Implementation Details
- Create via Django admin
- Avatar personas:
  - "Budget Buddy" - General budgeting expert
  - "DIY Dan" - DIY and repairs specialist
  - "Thrifty Tina" - Shopping and deals expert
- Configure:
  - cooldown_minutes: 30
  - max_posts_per_day: 10
  - temperature: 0.7

### Testing Requirements
- Trigger avatar participation
- Review avatar posts
- Verify cooldown works
- Expected output: AI avatars posting quality responses

---

## BUXMAX-126: Monitor System Performance

**Type**: Setup
**Priority**: High
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-125

### Description
Set up monitoring dashboards and alerts for system health and performance.

### Acceptance Criteria
- [ ] Monitoring dashboards configured
- [ ] Key metrics tracked (response time, error rate, task queue length)
- [ ] Alerts configured for critical issues
- [ ] Daily/weekly reports set up
- [ ] Cost tracking dashboard

### Implementation Details
- Use Flower for Celery monitoring
- Use Sentry for error tracking
- Create custom dashboard for:
  - Scraping statistics
  - AI generation costs
  - User activity
  - Content moderation stats

### Testing Requirements
- Access dashboards
- Verify metrics updating
- Test alerts
- Expected output: Comprehensive monitoring in place

---

## BUXMAX-127: Gather User Feedback

**Type**: Setup
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-126

### Description
Implement user feedback mechanisms and begin collecting feedback.

### Acceptance Criteria
- [ ] Feedback form created
- [ ] Feedback link in footer
- [ ] Email notifications for feedback
- [ ] Feedback stored in database
- [ ] Feedback review process established

### Implementation Details
- Create simple feedback form
- Add to site footer
- Store in database or send via email
- Review feedback weekly

### Testing Requirements
- Submit test feedback
- Verify receipt
- Expected output: Feedback mechanism working

---

## BUXMAX-128: Optimize Performance

**Type**: Configuration
**Priority**: Medium
**Complexity**: Medium (3-6 hours)
**Dependencies**: BUXMAX-126

### Description
Analyze performance metrics and optimize slow queries, views, and tasks.

### Acceptance Criteria
- [ ] Slow queries identified and optimized
- [ ] Database indexes added where needed
- [ ] Caching implemented for expensive operations
- [ ] Task execution times reduced
- [ ] Page load times <2 seconds

### Implementation Details
- Use Django Debug Toolbar to identify slow queries
- Add select_related() and prefetch_related()
- Implement caching for:
  - Article lists
  - Forum topic lists
  - User profiles
- Optimize Celery tasks

### Testing Requirements
- Run performance tests
- Compare before/after metrics
- Expected output: Improved performance

---

## BUXMAX-129: Create User Documentation

**Type**: Documentation
**Priority**: Medium
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-127

### Description
Create user-facing documentation including FAQ, how-to guides, and community guidelines.

### Acceptance Criteria
- [ ] FAQ page created
- [ ] How-to guides for main features
- [ ] Community guidelines
- [ ] Privacy policy
- [ ] Terms of service
- [ ] About page

### Implementation Details
- Files to create:
  - `templates/pages/faq.html`
  - `templates/pages/how_to.html`
  - `templates/pages/guidelines.html`
  - `templates/pages/privacy.html`
  - `templates/pages/terms.html`
  - `templates/pages/about.html`

### Testing Requirements
- Review all pages
- Verify links work
- Expected output: Comprehensive user documentation

---

## BUXMAX-130: Plan Next Iteration

**Type**: Documentation
**Priority**: Low
**Complexity**: Small (1-2 hours)
**Dependencies**: BUXMAX-129

### Description
Review launch metrics, gather feedback, and plan next iteration of features and improvements.

### Acceptance Criteria
- [ ] Launch metrics reviewed
- [ ] User feedback analyzed
- [ ] Issues prioritized
- [ ] Next iteration roadmap created
- [ ] New tickets created for next phase
- [ ] Team retrospective conducted

### Implementation Details
- Review metrics:
  - User signups
  - Content engagement
  - AI generation costs
  - System performance
  - Error rates
- Identify top priorities for next iteration
- Create new tickets in issue tracker

### Testing Requirements
- Review all metrics
- Document findings
- Expected output: Clear roadmap for next iteration

---

# Summary

This ticket list provides a comprehensive, step-by-step implementation plan for the Frugal Living Content Aggregation and Generation Platform. The 130 tickets are organized into 10 phases, each building on the previous phase to create a fully functional, production-ready application.

## Key Statistics

- **Total Tickets**: 130
- **Critical Priority**: 25 tickets
- **High Priority**: 45 tickets
- **Medium Priority**: 45 tickets
- **Low Priority**: 15 tickets

## Estimated Timeline

- **Phase 1 (Foundation)**: 1-2 weeks
- **Phase 2 (Data Models)**: 2-3 weeks
- **Phase 3 (Scraping)**: 2-3 weeks
- **Phase 4 (Celery Tasks)**: 2-3 weeks
- **Phase 5 (AI Integration)**: 2-3 weeks
- **Phase 6 (Frontend)**: 2-3 weeks
- **Phase 7 (Moderation)**: 1-2 weeks
- **Phase 8 (Testing)**: 1-2 weeks
- **Phase 9 (Deployment)**: 1 week
- **Phase 10 (Launch)**: 1 week

**Total Estimated Time**: 15-23 weeks (4-6 months)

## Dependencies

The tickets are structured with clear dependencies to enable:
- **Parallel work**: Multiple developers can work on independent tickets simultaneously
- **Incremental progress**: Each phase builds on previous phases
- **Testability**: Tests can be written alongside implementation
- **Flexibility**: Tickets can be reordered within phases as needed

## Usage

1. **For AI Coding Agents**: Start with BUXMAX-001 and proceed sequentially, checking dependencies before starting each ticket
2. **For Development Teams**: Assign tickets based on expertise and dependencies, allowing parallel work where possible
3. **For Project Managers**: Use this as a sprint planning guide, grouping tickets into 2-week sprints

## Next Steps

1. Review and prioritize tickets based on business needs
2. Assign tickets to team members or AI agents
3. Set up project tracking (Jira, GitHub Projects, etc.)
4. Begin implementation with Phase 1
5. Conduct regular reviews and adjust priorities as needed

---

**Document Version**: 1.0
**Last Updated**: 2025-10-01
**Reference**: docs/enhanced_plan.md


