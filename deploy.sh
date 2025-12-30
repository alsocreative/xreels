#!/bin/bash
npx wrangler pages deploy . --project-name dopa-meme-hu --commit-dirty=true > deploy.log 2>&1
