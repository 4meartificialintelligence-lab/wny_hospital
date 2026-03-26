openclaw config set agents.defaults.model.primary "custom-api-deepseek-com/deepseek-reasoner"

openclaw config set agents.defaults.model.fallbacks '["custom-api-deepseek-com/deepseek-reasoner","opencode-go/minimax-m2.5", "google/gemini-3.1-pro-preview","openrouter/free"]' --strict-json

{
  "meta": {
    "lastTouchedVersion": "2026.3.13",
    "lastTouchedAt": "2026-03-26T15:19:45.232Z"
  },
  "wizard": {
    "lastRunAt": "2026-03-26T15:19:45.068Z",
    "lastRunVersion": "2026.3.13",
    "lastRunCommand": "configure",
    "lastRunMode": "local"
  },
  "auth": {
    "profiles": {
      "google-gemini-cli:bankzza555666@gmail.com": {
        "provider": "google-gemini-cli",
        "mode": "oauth",
        "email": "bankzza555666@gmail.com"
      },
      "google:default": {
        "provider": "google",
        "mode": "api_key"
      },
      "openrouter:default": {
        "provider": "openrouter",
        "mode": "api_key"
      },
      "google-gemini-cli:4me.artificial.intelligence@gmail.com": {
        "provider": "google-gemini-cli",
        "mode": "oauth",
        "email": "4me.artificial.intelligence@gmail.com"
      },
      "opencode-go:default": {
        "provider": "opencode-go",
        "mode": "api_key"
      },
      "deepseek:default": {
        "provider": "deepseek",
        "mode": "api_key"
      }
    }
  },
  "models": {
    "mode": "merge",
    "providers": {
      "custom-api-deepseek-com": {
        "baseUrl": "https://api.deepseek.com/v1",
        "apiKey": "sk-f3ce4d1ce44649768b3308ec95b5a8d1",
        "api": "openai-completions",
        "models": [
          {
            "id": "deepseek-reasoner",
            "name": "deepseek-reasoner (Custom Provider)",
            "reasoning": false,
            "input": [
              "text"
            ],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 16000,
            "maxTokens": 4096
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "custom-api-deepseek-com/deepseek-reasoner",
        "fallbacks": [
          "google/gemini-3.1-pro-preview",
          "openrouter/openai/gpt-oss-120b:free",
          "openrouter/qwen/qwen3-coder:free",
          "openrouter/z-ai/glm-4.5-air:free",
          "opencode/minimax-m2.5-free",
          "opencode/mimo-v2-flash-free",
          "openrouter/arcee-ai/trinity-large-preview:free",
          "openrouter/arcee-ai/trinity-mini:free",
          "openrouter/free",
          "deepseek/deepseek-chat",
          "deepseek/deepseek-reasoner"
        ]
      },
      "models": {
        "google/gemini-3.1-pro-preview": {},
        "openrouter/auto": {
          "alias": "OpenRouter"
        },
        "openrouter/openai/gpt-oss-120b:free": {},
        "openrouter/qwen/qwen3-coder:free": {},
        "openrouter/z-ai/glm-4.5-air:free": {},
        "opencode/minimax-m2.5-free": {},
        "opencode/mimo-v2-flash-free": {},
        "openrouter/arcee-ai/trinity-large-preview:free": {},
        "openrouter/arcee-ai/trinity-mini:free": {},
        "openrouter/free": {},
        "opencode-go/kimi-k2.5": {
          "alias": "Kimi"
        },
        "opencode-go/glm-5": {
          "alias": "GLM"
        },
        "opencode-go/minimax-m2.5": {
          "alias": "MiniMax"
        },
        "deepseek/deepseek-chat": {
          "alias": "Deepseek-V3"
        },
        "deepseek/deepseek-reasoner": {
          "alias": "Deepseek-R1"
        },
        "custom-api-deepseek-com/deepseek-reasoner": {
          "alias": "DEEPSEEKR1"
        }
      },
      "workspace": "/home/nn/.openclaw/workspace"
    },
    "list": [
      {
        "id": "main",
        "tools": {
          "alsoAllow": [
            "read"
          ]
        }
      }
    ]
  },
  "tools": {
    "profile": "coding",
    "web": {
      "search": {
        "enabled": true,
        "provider": "brave",
        "apiKey": "."
      }
    }
  },
  "messages": {
    "tts": {
      "provider": "edge",
      "edge": {
        "enabled": true,
        "voice": "th-TH-NiwatNeural",
        "lang": "th-TH"
      }
    }
  },
  "commands": {
    "native": "auto",
    "nativeSkills": "auto",
    "restart": true,
    "ownerDisplay": "raw"
  },
  "session": {
    "dmScope": "per-channel-peer"
  },
  "hooks": {
    "internal": {
      "enabled": true,
      "entries": {
        "session-memory": {
          "enabled": true
        }
      }
    }
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "dmPolicy": "open",
      "botToken": "8043522097:AAHrced_FP21eY4xsavv8JjRE097dvFT4Dw",
      "allowFrom": [
        "*"
      ],
      "groupAllowFrom": [],
      "groupPolicy": "allowlist",
      "streaming": "partial"
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "lan",
    "controlUi": {
      "allowedOrigins": [
        "https://nnb.netfree.in.th",
        "https://nn.tail977854.ts.net"
      ]
    },
    "auth": {
      "mode": "token",
      "token": "8c382554bc8fd6b5997613f019873f1750bd169ac935cd2b"
    },
    "tailscale": {
      "mode": "off",
      "resetOnExit": false
    },
    "remote": {
      "url": "wss://nnb.netfree.in.th",
      "token": "4d31add19e907bc2cd614c38cfffdf1420fcf25de7f43578"
    },
    "nodes": {
      "denyCommands": [
        "camera.snap",
        "camera.clip",
        "screen.record",
        "contacts.add",
        "calendar.add",
        "reminders.add",
        "sms.send"
      ]
    }
  },
  "plugins": {
    "entries": {
      "telegram": {
        "enabled": true
      },
      "google-gemini-cli-auth": {
        "enabled": true
      }
    }
  }
}
nn@nn:~$
