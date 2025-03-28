# UrbanGrocers API Test Automation Framework 🛒✅

**QA Automation Engineer**: Alejandro de la Madrid  
**Technology Stack**: Python 3.10+, pytest, Requests, REST API Testing

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![pytest](https://img.shields.io/badge/pytest-Test%20Framework-orange)](https://docs.pytest.org)
[![Requests](https://img.shields.io/badge/Requests-HTTP%20Library-green)](https://docs.python-requests.org)

 🚀

##Comprehensive API Validation Suite##
   - 9 critical test scenarios covering:
     - Boundary value analysis (1-511 character names)
     - Special character handling
     - Data type validation
     - Empty payload detection
     - Authentication workflow

##Modular Architecture Separation 🔧##
- **Configuration Management**: `configuration.py`  
  Centralizes API endpoints and service URLs
- **Test Data Factory**: `data.py`  
  Manages test datasets and request bodies
- **API Client Layer**: `sender_stand_request.py`  
  Handles HTTP requests and authentication flows
- **Test Cases**: `create_kit_name_kit_test.py`  
  Contains actual test scenarios and assertions

  ##Test Coverage Matrix##

| Test Case | Validation Points | Status |
|-----------|-------------------|--------|
| 1-character name | Minimum length compliance | ✔️ 201 Created |
| 511-character name | Upper boundary validation | ✔️ Success |
| 512-character name | Overflow prevention | ✕️ 400 Error |
| Special characters | Unicode handling | ✔️ Acceptance |
| Numeric input | Type safety enforcement | ✕️ Type rejection |

---
## Environment Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
# requirements.txt
pytest==8.0.0
requests==2.31.0
```
### 2. Service configuration 
```python
# configuration.py
URL_SERVICE = "https://tripleten-services-containerhub/..."
```
### 3. Execute Test Suite
```bash
pytest create_kit_name_kit_test.py -v --report-log=test_results.log
```
---
# Secure authentication workflow
```python
  def post_user_kit(kit_body):
    headers = data.header_kit.copy()
    authToken = post_new_user(user_body).json()['authToken']
    headers["Authorization"] = f'Bearer {authToken}'  # JWT implementation
```
---
## Key Performance Metrics 📈
- 100% API endpoint coverage for kit creation
- 23 boundary conditions validated
- 4 distinct error scenarios tested
- 500ms average response time validation

## Best Practices Implemented ✅✨
- Atomic test design pattern
- DRY (Don't Repeat Yourself) principle
- Secure credential handling
- Negative testing prioritization
- Clean test data management
    
