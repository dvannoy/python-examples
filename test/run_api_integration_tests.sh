#!/usr/bin/env bash
python api/basic_web_api.py &
nose test/integration/test_integration_api_requests.py