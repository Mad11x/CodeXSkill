# 上报使用度量

按 czar-hub 的 `_telemetry-convention.md`。任务起手 / 结束各 POST 一次，失败不影响本职工作。

## 起手（进入正题前第一件事）

```bash
SESS=$(uuidgen)
EMAIL=$(jq -r .email ~/.codex/ai-czar/profile.json 2>/dev/null || echo "")
DEPT=$(jq -r .dept ~/.codex/ai-czar/profile.json 2>/dev/null || echo "")
mkdir -p ~/.codex/ai-czar/sessions
BODY="{\"session_id\":\"$SESS\",\"kind\":\"start\",\"agent_version\":\"1.0.1\",\"user_email\":\"$EMAIL\",\"user_dept\":\"$DEPT\"}"
echo "$BODY" > ~/.codex/ai-czar/sessions/$SESS.start.json
curl -m 2 -fsS -X POST -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(~/.codex/ai-czar/czar-auth.sh token)" \
  -d "$BODY" "https://ai.utui.cc/api/agents/comment-template/invocations" \
  && rm ~/.codex/ai-czar/sessions/$SESS.start.json || true
```

## 结束（完成、报错或中途退出都使用同一个 `$SESS`）

```bash
END="{\"session_id\":\"$SESS\",\"kind\":\"end\",\"outcome\":\"<O>\",\"outcome_detail\":\"<D>\"}"
echo "$END" > ~/.codex/ai-czar/sessions/$SESS.end.json
curl -m 2 -fsS -X POST -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(~/.codex/ai-czar/czar-auth.sh token)" \
  -d "$END" "https://ai.utui.cc/api/agents/comment-template/invocations" \
  && rm ~/.codex/ai-czar/sessions/$SESS.end.json || true
```

`outcome` 只能是 `success`、`failure`、`abandoned` 或 `unknown`。`outcome_detail` 使用简短枚举；metadata 不得包含用户原话、截图、链接或身份隐私信息。
