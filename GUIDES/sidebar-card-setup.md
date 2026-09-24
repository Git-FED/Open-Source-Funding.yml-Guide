# Sidebar Card Setup

The repository sidebar is the most visible funding surface on GitHub. It uses two layers:

1. `.github/FUNDING.yml` tells GitHub which links to expose.
2. **Settings → Features → Sponsorships** turns the repository-level card on.

A file alone may not be enough when a repository was created through the CLI or an API.

## Checklist

- [ ] Put `.github/FUNDING.yml` on the default branch.
- [ ] Use supported keys and valid usernames.
- [ ] Open repository **Settings → General → Features**.
- [ ] Enable **Sponsorships** or choose **Set up sponsor button**.
- [ ] Visit the repository while signed out or in an incognito window.
- [ ] Click the Sponsor button and test every link.

GitHub Sponsors can appear as the native path. External services are typically listed behind the same Sponsor entry point. That makes a two-rail strategy useful: visitors do not need to navigate a wall of buttons in your README.

## Common failures

The file is on the wrong branch, the username is misspelled, a repository-level file overrides the intended account configuration, or the Sponsorships feature is still disabled. Fix one variable at a time and test from a clean browser session.
