# Project To-Do List

- [x] Finish the `create room` functionallity
- [x] Finish the `chat` functionallity
- [x] Change the `chat` functionallity to use WebSockets
- [x] Finish the `profile update` functionallity
- [x] Finish reset password functionallity
- [ ] Send password reset email in the custom domain
- [ ] Figure out uid64 and token
- [ ] Use class-based views
- [x] Write tests
- [ ] Write more tests
- [ ] Write comments for functions and classes
- [ ] Make it a package for reuse
- [x] Learn docker
- [x] Regenerate the secret key

# Test Coverage Report

As part of our commitment to maintain high-quality code, we regularly run tests to cover various parts of our application. Below is the latest test coverage report for our project:

| Module                                               | Stmts   | Miss   | Cover  |
| ---------------------------------------------------- | ------- | ------ | ------ |
| chatroom/**init**.py                                 | 0       | 0      | 100%   |
| chatroom/admin.py                                    | 17      | 1      | 94%    |
| chatroom/apps.py                                     | 4       | 0      | 100%   |
| chatroom/consumers.py                                | 28      | 1      | 96%    |
| chatroom/forms.py                                    | 10      | 0      | 100%   |
| chatroom/migrations/0001_initial.py                  | 7       | 0      | 100%   |
| chatroom/migrations/0002_rename_message_chatmessage  | 5       | 0      | 100%   |
| chatroom/migrations/**init**.py                      | 0       | 0      | 100%   |
| chatroom/models.py                                   | 13      | 0      | 100%   |
| chatroom/routing.py                                  | 3       | 3      | 0%     |
| chatroom/tests/**init**.py                           | 0       | 0      | 100%   |
| chatroom/tests/test_admin.py                         | 12      | 0      | 100%   |
| chatroom/tests/test_consumers.py                     | 26      | 0      | 100%   |
| chatroom/tests/test_forms.py                         | 10      | 0      | 100%   |
| chatroom/tests/test_models.py                        | 28      | 0      | 100%   |
| chatroom/tests/test_urls.py                          | 13      | 0      | 100%   |
| chatroom/tests/test_views.py                         | 39      | 6      | 85%    |
| chatroom/urls.py                                     | 4       | 0      | 100%   |
| chatroom/views.py                                    | 19      | 2      | 89%    |
| django_chatroom/**init**.py                          | 0       | 0      | 100%   |
| django_chatroom/asgi.py                              | 9       | 9      | 0%     |
| django_chatroom/settings.py                          | 34      | 0      | 100%   |
| django_chatroom/urls.py                              | 9       | 1      | 89%    |
| django_chatroom/wsgi.py                              | 4       | 4      | 0%     |
| manage.py                                            | 12      | 2      | 83%    |
| users/**init**.py                                    | 0       | 0      | 100%   |
| users/admin.py                                       | 7       | 0      | 100%   |
| users/apps.py                                        | 6       | 0      | 100%   |
| users/forms.py                                       | 18      | 0      | 100%   |
| users/migrations/0001_initial.py                     | 7       | 0      | 100%   |
| users/migrations/0002_alter_profile_profile_picture  | 4       | 0      | 100%   |
| users/migrations/**init**.py                         | 0       | 0      | 100%   |
| users/models.py                                      | 18      | 4      | 78%    |
| users/signals.py                                     | 11      | 0      | 100%   |
| users/tests/**init**.py                              | 0       | 0      | 100%   |
| users/tests/test_admin.py                            | 12      | 0      | 100%   |
| users/tests/test_forms.py                            | 12      | 1      | 92%    |
| users/tests/test_models.py                           | 9       | 0      | 100%   |
| users/tests/test_views.py                            | 10      | 0      | 100%   |
| users/views.py                                       | 30      | 19     | 37%    |
| ---------------------------------------------------- | ------- | ------ | ------ |
| TOTAL                                                | 450     | 53     | 88%    |

## Coverage Summary

- Total Statements: The total number of code statements in our project.
- Missed Statements: The number of statements in our code that are not covered by tests.
- Coverage: The percentage of our codebase that is covered by tests.

## Interpretation

- A high coverage percentage indicates a lower likelihood of undetected software bugs and higher code quality.
- We aim to maintain our coverage above a certain threshold (e.g., 80%) to ensure code reliability and maintainability.

## Continuous Improvement

- We are continuously working to improve our test coverage, especially in modules where it is below our desired threshold.
- Regular updates to this report will be provided to track our progress in enhancing test coverage.
