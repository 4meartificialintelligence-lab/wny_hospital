    },
    "qq": {
      "enabled": false,
      "appId": "",
      "secret": "",
      "allowFrom": [],
      "msgFormat": "plain"
    },
    "slack": {
      "enabled": false,
      "mode": "socket",
      "webhookPath": "/slack/events",
      "botToken": "",
      "appToken": "",
      "userTokenReadOnly": true,
      "replyInThread": true,
      "reactEmoji": "eyes",
      "allowFrom": [],
      "groupPolicy": "mention",
      "groupAllowFrom": [],
      "dm": {
        "enabled": true,
        "policy": "open",
        "allowFrom": []
      }
    },
    "telegram": {
      "enabled": true,
      "token": "8735746487:AAEjHnhte7ipUgy8cehFKX_EGW0isuqF094",
      "allowFrom": [],
      "proxy": null,
      "replyToMessage": false,
      "groupPolicy": "mention"
    },
    "wecom": {
      "enabled": false,
      "botId": "",
      "secret": "",
      "allowFrom": [],
      "welcomeMessage": ""
    },
    "whatsapp": {
      "enabled": false,
      "bridgeUrl": "ws://localhost:3001",
      "bridgeToken": "",
      "allowFrom": []
    }
  },
  "providers": {
    "gemini": {
      "apiKey": "AIzaSyCg5_nGo8ztX7-z6UHMDZa5KLTooxAmm0Q",
      "apiBase": null,
      "extraHeaders": null
    },
    "openai": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "anthropic": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "deepseek": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "openrouter": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "groq": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "zhipu": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "dashscope": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "vllm": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "ollama": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "moonshot": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "minimax": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "aihubmix": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "siliconflow": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "volcengine": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "volcengineCodingPlan": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "byteplus": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "byteplusCodingPlan": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "openaiCodex": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    },
    "githubCopilot": {
      "apiKey": "",
      "apiBase": null,
      "extraHeaders": null
    }
  },
  "gateway": {
    "host": "0.0.0.0",
    "port": 18790,
    "heartbeat": {
      "enabled": true,
      "intervalS": 1800
    }
  },
  "tools": {
    "web": {
      "proxy": null,
      "search": {
        "provider": "brave",
        "apiKey": "",
        "baseUrl": "",
        "maxResults": 5
      }
    },
    "exec": {
      "timeout": 60,
      "pathAppend": ""
    },
    "restrictToWorkspace": false,
    "mcpServers": {}
  }
}
