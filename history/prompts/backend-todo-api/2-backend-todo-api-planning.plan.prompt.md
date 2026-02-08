---
id: 2
title: backend-todo-api-planning
stage: plan
date_iso: 2026-02-06
surface: agent
model: gpt-4
feature: backend-todo-api
branch: 002-backend-todo-api
user: FC
command: sp.plan
labels:
  - planning
  - backend
  - api
  - jwt
  - authentication
links:
  spec: ../spec.md
  ticket: null
  adr: null
  pr: null
files_yaml:
  - E:\phase-3\specs\002-backend-todo-api\plan.md
  - E:\phase-3\specs\002-backend-todo-api\research.md
  - E:\phase-3\specs\002-backend-todo-api\data-model.md
  - E:\phase-3\specs\002-backend-todo-api\quickstart.md
  - E:\phase-3\specs\002-backend-todo-api\contracts\todo-api-openapi.yaml
tests_yaml: []
prompt_text: "$ARGUMENTS\n\nYou **MUST** consider the user input before proceeding (if not empty).\n\n## Outline\n\n1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like \"I'm Groot\", use escape syntax: e.g 'I'\\''m Groot' (or double-quote if possible: \"I'm Groot\").\n\n2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).\n\n3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:\n   - Fill Technical Context (mark unknowns as \"NEEDS CLARIFICATION\")\n   - Fill Constitution Check section from constitution\n   - Evaluate gates (ERROR if violations unjustified)\n   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)\n   - Phase 1: Generate data-model.md, contracts/, quickstart.md\n   - Phase 1: Update agent context by running the agent script\n   - Re-evaluate Constitution Check post-design\n\n4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.\n\n## Phases\n\n### Phase 0: Outline & Research\n\n1. **Extract unknowns from Technical Context** above:\n   - For each NEEDS CLARIFICATION → research task\n   - For each dependency → best practices task\n   - For each integration → patterns task\n\n2. **Generate and dispatch research agents**:\n\n   ```text\n   For each unknown in Technical Context:\n     Task: \"Research {unknown} for {feature context}\"\n   For each technology choice:\n     Task: \"Find best practices for {tech} in {domain}\"\n   ```\n\n3. **Consolidate findings** in `research.md` using format:\n   - Decision: [what was chosen]\n   - Rationale: [why chosen]\n   - Alternatives considered: [what else evaluated]\n\n**Output**: research.md with all NEEDS CLARIFICATION resolved\n\n### Phase 1: Design & Contracts\n\n**Prerequisites:** `research.md` complete\n\n1. **Extract entities from feature spec** → `data-model.md`:\n   - Entity name, fields, relationships\n   - Validation rules from requirements\n   - State transitions if applicable\n\n2. **Generate API contracts** from functional requirements:\n   - For each user action → endpoint\n   - Use standard REST/GraphQL patterns\n   - Output OpenAPI/GraphQL schema to `/contracts/`\n\n3. **Agent context update**:\n   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType qwen`\n   - These scripts detect which AI agent is in use\n   - Update the appropriate agent-specific context file\n   - Add only new technology from current plan\n   - Preserve manual additions between markers\n\n**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file\n\n## Key rules\n\n- Use absolute paths\n- ERROR on gate failures or unresolved clarifications\n\n---\n\nAs the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.\n\n1) Determine Stage\n   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general\n\n2) Generate Title and Determine Routing:\n   - Generate Title: 3–7 words (slug for filename)\n   - Route is automatically determined by stage:\n     - `constitution` → `history/prompts/constitution/`\n     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)\n     - `general` → `history/prompts/general/`\n\n3) Create and Fill PHR (Shell first; fallback agent‑native)\n   - Run: `.specify/scripts/bash/create-phr.sh --title \"<title>\" --stage <stage> [--feature <name>] --json`\n   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.\n   - If the script fails:\n     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)\n     - Allocate an ID; compute the output path based on stage from step 2; write the file\n     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT\n\n4) Validate + report\n   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.\n   - On failure: warn, don't block. Skip only for `/sp.phr`."
response_text: "I've completed the implementation planning for the Backend Todo API with JWT Authentication. Here's what was accomplished:\n\n1. Created the implementation plan at `E:\\phase-3\\specs\\002-backend-todo-api\\plan.md` with:\n   - Technical context filled in\n   - Constitution check passed with all gates verified\n   - Project structure defined\n   - Phase completion status updated\n\n2. Completed Phase 0 (Research) by creating `research.md` with key technology decisions\n\n3. Completed Phase 1 (Design & Contracts) by creating:\n   - `data-model.md` with entity definitions\n   - API contracts in the `contracts/` directory (OpenAPI specification)\n   - `quickstart.md` with setup instructions\n\n4. Updated the agent context with the new technology stack\n\nAll required artifacts have been generated according to the plan template. The implementation plan is now ready for the next phase, which would typically be creating the development tasks from this plan (/sp.tasks)."
outcome: The implementation planning for the Backend Todo API with JWT Authentication is complete. All required artifacts have been created according to the plan template, including the implementation plan, research findings, data model, API contracts, and quickstart guide. The agent context has been updated with the new technology stack.
evaluation: The planning phase was executed successfully with all required artifacts created. The plan aligns with the constitution and feature specification. All gates in the constitution check were passed. The project structure and technical context are clearly defined.
---