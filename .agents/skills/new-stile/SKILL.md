---
name: new-stile
description: Use a modern Bootstrap 5 UI with:
- Automatic dark/light mode using data-bs-theme="auto"
- CSS variables adapting to prefers-color-scheme
- Glassmorphism and neumorphism reusable classes
- Smooth micro-interactions using GSAP
- Fully accessible components (ARIA roles, keyboard navigation, good contrast)
- Clean, responsive layout using Bootstrap utilities
---

<!-- Tip: Use /create-skill in chat to generate content with agent assistance -->

This skill provides a reusable visual and interaction system for modern Bootstrap 5 pages.

## Goals

- Build a clear, polished UI with Bootstrap utilities and custom tokens.
- Support automatic light and dark mode without duplicating markup.
- Provide reusable surface styles (glass and neo) for cards, panels, and sections.
- Improve perceived quality with subtle, meaningful motion.
- Keep components accessible with keyboard support and ARIA semantics.

## Use This Skill When

- Creating or redesigning templates with Bootstrap 5.
- Building dashboards, forms, lists, cards, or landing sections.
- You need consistent theming across pages.
- You need animation polish without heavy visual noise.

## Mandatory Rules

1. Set theme mode on the root element:
	 - Add data-bs-theme="auto" in the html tag.
2. Define CSS variables for both color schemes.
3. Use reusable classes for elevated surfaces.
4. Keep animation short and purposeful.
5. Include accessibility basics in every component:
	 - Visible focus state.
	 - Keyboard reachable controls.
	 - ARIA labels where native semantics are not enough.
	 - Color contrast high enough for body text.

## Implementation Pattern

### 1) Base Theme Structure

Add this in your base template root:

```html
<html lang="es" data-bs-theme="auto">
```

### 2) Theme Tokens

Define semantic tokens in CSS and adapt via prefers-color-scheme.

```css
:root {
	--app-bg: #f4f6f8;
	--app-surface: rgba(255, 255, 255, 0.72);
	--app-surface-solid: #ffffff;
	--app-text: #1f2933;
	--app-muted: #6b7280;
	--app-accent: #d4a017;
	--app-border: rgba(31, 41, 51, 0.12);
	--app-shadow: 0 12px 28px rgba(16, 24, 40, 0.12);
}

@media (prefers-color-scheme: dark) {
	:root {
		--app-bg: #0f1419;
		--app-surface: rgba(20, 27, 36, 0.65);
		--app-surface-solid: #1a2330;
		--app-text: #e5e7eb;
		--app-muted: #a3acb9;
		--app-accent: #f1c84a;
		--app-border: rgba(229, 231, 235, 0.16);
		--app-shadow: 0 12px 28px rgba(0, 0, 0, 0.38);
	}
}

body {
	background:
		radial-gradient(circle at 10% 10%, rgba(212, 160, 23, 0.08), transparent 35%),
		radial-gradient(circle at 90% 5%, rgba(59, 130, 246, 0.08), transparent 30%),
		var(--app-bg);
	color: var(--app-text);
}
```

### 3) Reusable Surfaces

```css
.glass {
	background: var(--app-surface);
	border: 1px solid var(--app-border);
	box-shadow: var(--app-shadow);
	backdrop-filter: blur(10px);
	-webkit-backdrop-filter: blur(10px);
	border-radius: 1rem;
}

.neo {
	background: var(--app-surface-solid);
	border-radius: 1rem;
	box-shadow:
		8px 8px 18px rgba(15, 20, 25, 0.12),
		-8px -8px 18px rgba(255, 255, 255, 0.75);
}

@media (prefers-color-scheme: dark) {
	.neo {
		box-shadow:
			8px 8px 18px rgba(0, 0, 0, 0.5),
			-8px -8px 18px rgba(255, 255, 255, 0.03);
	}
}
```

### 4) Motion with GSAP

Use motion for hierarchy only (entry, emphasis, no constant distractions).

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.7/dist/gsap.min.js"></script>
<script>
	gsap.from(".reveal", {
		y: 20,
		opacity: 0,
		duration: 0.45,
		stagger: 0.06,
		ease: "power2.out"
	});
</script>
```

### 5) Accessibility Pattern

- Use native elements first (button, nav, table, form, label).
- Add aria-label when button text is ambiguous.
- Ensure tab order follows visual flow.
- Keep focus visible:

```css
:focus-visible {
	outline: 3px solid color-mix(in srgb, var(--app-accent) 70%, white 30%);
	outline-offset: 2px;
}
```

## Bootstrap Composition Guidance

- Prefer container-fluid + constrained inner wrappers for admin pages.
- Use row g-3 or g-4 for rhythmic spacing.
- For dense tables, use table-sm and align-middle.
- Keep forms readable with consistent max widths:
	- Quick forms: col-lg-6
	- Medium forms: col-lg-8
	- Full forms: col-lg-10 or col-xl-8

## Example Markup

```html
<section class="container-fluid py-4">
	<div class="container">
		<div class="glass p-4 reveal" role="region" aria-label="Panel de sucursales">
			<div class="d-flex justify-content-between align-items-center mb-3">
				<h2 class="h4 mb-0">Sucursales</h2>
				<button class="btn btn-warning">Nueva sucursal</button>
			</div>

			<div class="table-responsive">
				<table class="table table-sm align-middle mb-0" aria-label="Listado de sucursales">
					<thead>
						<tr>
							<th>Nombre</th>
							<th>Direccion</th>
							<th class="text-end">Acciones</th>
						</tr>
					</thead>
				</table>
			</div>
		</div>
	</div>
</section>
```

## Anti-Patterns

- Do not animate every element.
- Do not remove focus styles.
- Do not hardcode colors in many selectors; use tokens.
- Do not mix many card styles in one page without purpose.
- Do not rely only on color to communicate status.

## Definition of Done

- Theme auto mode is active and works in light/dark environments.
- UI uses tokens and reusable surface classes.
- Motion is subtle and non-blocking.
- Components are keyboard and screen-reader friendly.
- Layout is responsive and visually consistent on mobile and desktop.