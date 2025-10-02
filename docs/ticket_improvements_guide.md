# Ticket Improvements Guide

## Overview

This document provides a systematic guide for improving all 130 tickets in `docs/enhanced_tickets.md` to achieve 90%+ AI agent completion rate. Rather than creating a massive 15,000+ line file, this guide provides:

1. **Improvement Templates** - Reusable patterns for fixing common issues
2. **Complete Rewrites** - Full improved versions of the 5 weakest tickets
3. **Configuration Appendix** - All configuration values referenced in tickets
4. **Systematic Fix Instructions** - How to apply improvements to remaining tickets

---

## Improvement Templates

### Template 1: Eliminating Vague Qualifiers

**BEFORE (Vague)**:
```markdown
- [ ] Handles errors gracefully
- [ ] Uses appropriate timeout values
- [ ] Implements proper error logging
```

**AFTER (Specific)**:
```markdown
- [ ] Catches `scrapy.exceptions.IgnoreRequest`, `requests.exceptions.Timeout`, and `Exception`
- [ ] Sets timeout=30 seconds for HTTP requests, timeout=60 seconds for AI API calls
- [ ] Logs errors with `logger.error(f"Error in {function_name}: {str(e)}", exc_info=True)`
```

### Template 2: Completing Code Examples

**BEFORE (Placeholder)**:
```python
def scrape_source(self, source_id):
    # Run spider
    process.start()
    return {'success': True, 'items_scraped': 10}  # Placeholder
```

**AFTER (Complete)**:
```python
def scrape_source(self, source_id):
    from scrapy.crawler import CrawlerRunner
    from scrapy.utils.project import get_project_settings
    from twisted.internet import reactor, defer
    
    source = Source.objects.get(id=source_id)
    
    # Configure runner
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    
    # Select spider based on source type
    spider_map = {
        'rss': 'scrapers.spiders.rss_spider.RSSSpider',
        'blog': 'scrapers.spiders.blog_spider.BlogSpider',
    }
    spider_class = spider_map.get(source.source_type)
    
    if not spider_class:
        raise ValueError(f"Unknown source_type: {source.source_type}")
    
    # Run spider
    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(spider_class, source_id=source_id)
        reactor.stop()
    
    crawl()
    reactor.run()
    
    # Get statistics
    stats = runner.crawlers[0].stats.get_stats()
    items_scraped = stats.get('item_scraped_count', 0)
    errors = stats.get('log_count/ERROR', 0)
    
    # Update source
    source.last_checked_at = timezone.now()
    source.items_scraped_count = items_scraped
    source.status = 'active' if errors == 0 else 'error'
    source.save()
    
    return {
        'success': errors == 0,
        'items_scraped': items_scraped,
        'errors': errors,
        'source_id': source_id
    }
```

### Template 3: Service Class Clarification

**BEFORE (Ambiguous)**:
```markdown
### Implementation Details
- Use ScraperService to manage spiders
- Call service.scrape_source(source_id)
```

**AFTER (Explicit)**:
```markdown
### Implementation Details

**Service Class Status**: CREATE NEW FILE

**File to create**: `apps/aggregation/services.py`

**Complete Service Class**:
```python
# apps/aggregation/services.py
from django.utils import timezone
from apps.aggregation.models import Source
import logging

logger = logging.getLogger(__name__)

class ScraperService:
    """Service for managing web scraping operations."""
    
    def __init__(self):
        self.spider_map = {
            'rss': 'scrapers.spiders.rss_spider.RSSSpider',
            'blog': 'scrapers.spiders.blog_spider.BlogSpider',
        }
    
    def scrape_source(self, source_id: int) -> dict:
        """Execute scraping for a single source."""
        # [Complete implementation as shown in Template 2]
    
    def get_spider_class(self, source_type: str):
        """Get spider class for source type."""
        spider_path = self.spider_map.get(source_type)
        if not spider_path:
            raise ValueError(f"Unknown source_type: {source_type}")
        return spider_path
```
```

### Template 4: Expanding Testing Requirements

**BEFORE (Vague)**:
```markdown
### Testing Requirements
- Test with mock spider
- Verify source updates
- Run: `pytest apps/aggregation/tests/test_services.py`
```

**AFTER (Specific)**:
```markdown
### Testing Requirements

**Test File**: `apps/aggregation/tests/test_services.py`

**Test 1: Successful Scraping**
```python
import pytest
from unittest.mock import patch, MagicMock
from apps.aggregation.services import ScraperService
from apps.aggregation.models import Source

@pytest.mark.django_db
class TestScraperService:
    
    def test_scrape_source_success(self):
        # Setup
        source = Source.objects.create(
            url='https://example.com/feed',
            source_type='rss',
            status='pending'
        )
        service = ScraperService()
        
        # Mock spider execution
        with patch('scrapy.crawler.CrawlerRunner') as mock_runner:
            mock_stats = {
                'item_scraped_count': 5,
                'log_count/ERROR': 0,
                'finish_reason': 'finished'
            }
            mock_runner.return_value.crawlers = [
                MagicMock(stats=MagicMock(get_stats=lambda: mock_stats))
            ]
            
            # Execute
            result = service.scrape_source(source.id)
        
        # Assertions
        assert result['success'] is True
        assert result['items_scraped'] == 5
        assert result['errors'] == 0
        
        # Verify source updated
        source.refresh_from_db()
        assert source.status == 'active'
        assert source.items_scraped_count == 5
        assert source.last_checked_at is not None
```

**Test 2: Scraping with Errors**
```python
    def test_scrape_source_with_errors(self):
        # Setup
        source = Source.objects.create(
            url='https://example.com/feed',
            source_type='rss',
            status='pending'
        )
        service = ScraperService()
        
        # Mock spider with errors
        with patch('scrapy.crawler.CrawlerRunner') as mock_runner:
            mock_stats = {
                'item_scraped_count': 2,
                'log_count/ERROR': 3,
                'finish_reason': 'finished'
            }
            mock_runner.return_value.crawlers = [
                MagicMock(stats=MagicMock(get_stats=lambda: mock_stats))
            ]
            
            # Execute
            result = service.scrape_source(source.id)
        
        # Assertions
        assert result['success'] is False
        assert result['items_scraped'] == 2
        assert result['errors'] == 3
        
        # Verify source marked as error
        source.refresh_from_db()
        assert source.status == 'error'
```

**Run Tests**:
```bash
pytest apps/aggregation/tests/test_services.py::TestScraperService -v
```

**Expected Output**:
```
test_scrape_source_success PASSED
test_scrape_source_with_errors PASSED

2 passed in 0.45s
```
```

### Template 5: Adding Prerequisites and Verification

**Add to every ticket**:

```markdown
### Prerequisites
- [List specific tickets that must be complete]
- [List specific files that must exist]
- [List specific packages that must be installed]

### Step-by-Step Implementation
1. [First concrete action]
2. [Second concrete action]
3. [Continue with numbered steps]

### Verification Checklist
- [ ] [Specific verification step 1]
- [ ] [Specific verification step 2]
- [ ] [Can run without errors]
- [ ] [Tests pass]
```

---

## Configuration Appendix

### User Agent Strings (for BUXMAX-042)

```python
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
]
```

### Scrape Frequencies (for BUXMAX-121)

```python
from datetime import timedelta

SCRAPE_FREQUENCIES = {
    'blog': timedelta(hours=24),      # Personal blogs update daily
    'news': timedelta(hours=6),       # News sites update frequently
    'forum': timedelta(hours=12),     # Forums have moderate activity
    'rss': timedelta(hours=12),       # RSS feeds vary
    'podcast': timedelta(days=7),     # Podcasts weekly
}
```

### Quality Criteria (for BUXMAX-121)

```python
QUALITY_CRITERIA = {
    'min_domain_authority': 30,        # Moz Domain Authority
    'min_update_frequency_days': 30,   # Updated at least monthly
    'min_content_length': 500,         # Average article length
    'max_ad_ratio': 0.30,             # Ad-to-content ratio
    'requires_robots_txt_allow': True, # Must allow scraping
    'min_https': True,                 # Must use HTTPS
}
```

### Engagement Metrics (for BUXMAX-053)

```python
ENGAGEMENT_METRICS = {
    'view_weight': 1.0,
    'comment_weight': 5.0,
    'share_weight': 10.0,
    'time_decay_days': 7,  # Older content gets lower score
}

def calculate_engagement_score(content):
    """Calculate engagement score for content selection."""
    from datetime import timedelta
    from django.utils import timezone
    
    age_days = (timezone.now() - content.published_at).days
    time_factor = max(0, 1 - (age_days / ENGAGEMENT_METRICS['time_decay_days']))
    
    score = (
        content.view_count * ENGAGEMENT_METRICS['view_weight'] +
        content.comment_count * ENGAGEMENT_METRICS['comment_weight'] +
        content.share_count * ENGAGEMENT_METRICS['share_weight']
    ) * time_factor
    
    return score
```

---

## Complete Rewrites of Top 5 Weakest Tickets

[The next sections will contain complete improved versions of BUXMAX-121, BUXMAX-053, BUXMAX-063, BUXMAX-075, and BUXMAX-041]

---

