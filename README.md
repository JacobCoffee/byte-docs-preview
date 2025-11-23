# Byte Bot Documentation Preview

This repository hosts preview builds of the [Byte Bot](https://github.com/JacobCoffee/byte) documentation for pull requests.

## How It Works

1. **Automatic Deployment**: When a PR is opened in the main `byte` repository, the CI workflow builds the documentation and deploys it to this repository under a directory named after the PR number.

2. **Preview Access**: Documentation previews are accessible at:
   ```
   https://jacobcoffee.github.io/byte-docs-preview/{PR_NUMBER}
   ```

3. **Automatic Cleanup**: A scheduled workflow runs daily to remove preview builds for closed or merged PRs, keeping the repository clean.

## Structure

- `/{PR_NUMBER}/` - Documentation preview for PR #{PR_NUMBER}
- `remove_stale.py` - Python script that removes stale preview builds
- `.github/workflows/remove_stale.yml` - GitHub Actions workflow for automated cleanup

## Maintenance

The repository is automatically maintained by GitHub Actions:
- **Deploy**: Triggered from the main `byte` repository when PRs are updated
- **Cleanup**: Runs daily at 1:00 AM UTC to remove stale previews

## Manual Cleanup

To manually trigger the cleanup workflow:
```bash
gh workflow run remove_stale.yml --repo JacobCoffee/byte-docs-preview
```

## Contributing

This repository is managed automatically. For issues related to documentation content, please open an issue in the [main byte repository](https://github.com/JacobCoffee/byte/issues).

## License

MIT - See the [main byte repository](https://github.com/JacobCoffee/byte) for license details.
