openclaw config set agents.defaults.model.primary "anthropic/claude-sonnet-4-6"

openclaw config set agents.defaults.model.fallbacks '["openai/gpt-5.2", "google/gemini-1.5-pro"]' --strict-json
