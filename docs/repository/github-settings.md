# GitHub configuration checklist

Repository: https://github.com/Seafood-City/K9

## Recorded starting state

At setup on November 9, 2026, K9 was public, its default branch was main, main was reported unprotected, and the repository contained README.md and an MIT LICENSE. The existing license is preserved.

The prepared configuration files should be committed through a pull request. They do not apply GitHub administration settings. The checklist below remains pending until an administrator applies and verifies each setting.

## General

In repository Settings, configure:

| Setting | Recommendation |
| --- | --- |
| Name / owner | K9 / Seafood-City |
| Description | Ground-only autonomous vehicle capstone using Jetson, Pixhawk and ZED 2i |
| Visibility | Existing public visibility retained; publish only team-owned or authorized material |
| Default branch | main |
| Issues | Enabled |
| Wiki | Disabled; use versioned docs/ |
| Discussions | Optional; leave off until there is a recurring need |
| Merge methods | Allow squash merging; disable merge commits and rebase merging |
| Squash commit default | Pull request title and description |
| Automatically delete head branches | Enabled |
| Suggest updating pull request branches | Enabled, if available |

Suggested topics: robotics, autonomous-vehicle, capstone, jetson, pixhawk, ardupilot, zed-camera.

## Protect main

First let the setup pull request's CI complete so the exact "Repository checks" status is known. Download main-ruleset.json from this folder, then use Settings > Rules > Rulesets > New ruleset > Import a ruleset. GitHub may label the sidebar Rulesets directly.

The JSON requests:

- Active protection of refs/heads/main.
- A pull request and one approving review from someone other than the author.
- Dismiss stale approvals when reviewable code changes.
- Resolve review conversations.
- A passing "Repository checks" job, with the branch up to date.
- Linear history, no force pushes and no deletion of main.
- No bypass actors.

Confirm that the status-check source is GitHub Actions in the UI after the check appears. Code-owner review is intentionally not required while CODEOWNERS contains only examples. Keep signed-commit enforcement off until every teammate has configured signing.

Importing the JSON activates protection; merely committing it does not. If rulesets are unavailable on the account's plan, apply the equivalent classic branch protection settings that the plan supports. Do not enable a required check with a different name or a check that never runs.

## Access and reviews

Give the four verified teammate accounts Write access, preferably through a dedicated organization team. Give Maintain to a repository coordinator and retain only the administrators needed for settings/recovery. Verify account identities before inviting or granting access.

Use the owner table to assign reviews, then replace commented CODEOWNERS examples with real accounts/teams that have Write access. Once those rules are verified, code-owner review can be enabled deliberately.

## Actions and dependency security

Under Actions > General:

- Allow organization actions, GitHub-owned actions and explicitly approved external actions.
- Keep the default workflow token at read access.
- Disable Actions creating or approving pull requests for this starter.
- Keep CI on GitHub-hosted runners. Do not expose an actuator-connected Jetson as a public pull-request runner.
- Review weekly Dependabot action-update pull requests. The initial actions are pinned to release commit SHAs.

Under the repository security settings, enable the available dependency graph, Dependabot alerts/security updates, secret scanning, push protection and private vulnerability reporting. UI labels and availability can differ by plan and organization policy.

Enable CodeQL for the actual supported source languages after implementation is imported; this scaffold does not pretend to analyze application code that is absent. Add dependency update entries when real package manifests are introduced.

## Verification after applying settings

- [ ] Setup pull request merged and Repository checks passed.
- [ ] main ruleset imported, active and visible on the repository.
- [ ] Direct pushes, force pushes and deletion of main are blocked.
- [ ] Pull requests require one teammate approval and the expected CI check.
- [ ] Squash merge, automatic branch deletion and Actions permissions verified.
- [ ] Correct teammate access and active CODEOWNERS rules verified.
- [ ] Available security features enabled.
- [ ] Large-file location and evidence access agreed by the team.

## Official references

- [Importing rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository)
- [Available rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [Secure use of Actions](https://docs.github.com/en/actions/reference/security/secure-use)
- [Repository security settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository)
