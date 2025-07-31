Generate comprehensive tests for this project based on the README and codebase. Create tests that actually verify the code does what the documentation claims. 

Testing Requirements: 

Read the README.md and identify every claim, feature, and example mentioned 

Create tests that verify each documented behavior actually works 

For every function/method, test: 

Normal inputs (happy path) 

Edge cases (empty, null, boundaries, zero, negative numbers) 

Invalid inputs (wrong types, malformed data) 

Error conditions (exceptions, failures) 

Integration tests that verify: 

Components work together correctly 

Data flows properly between modules 

APIs return what's documented 

File I/O operations work as described 

End-to-end tests for: 

Every example in the README 

Complete user workflows 

Command-line interfaces match documented usage 

Test quality requirements: 

Use descriptive test names that explain the scenario 

Include assertions that actually verify behavior, not just "no errors" 

Tests should fail if functionality breaks 

Mock external dependencies (APIs, databases, file systems) 

Each test should be independent 

Include both positive tests (it works) and negative tests (it fails appropriately) 

Coverage areas: 

Public API matches documentation 

Error messages are helpful and accurate 

Performance constraints mentioned in docs 

Security considerations if mentioned 

Configuration options work as documented 

Generate a complete test suite that would catch any discrepancy between what the README promises and what the code actually does. The tests should give confidence that the project works exactly as advertised. 

 