import { fontFamily } from 'tailwindcss/defaultTheme'
import colormap from 'colormap'

const jet = colormap({
	colormap: 'jet',
	nshades: 20,
	format: 'hex',
	alpha: 0.4
}).reduce((acc, color, i) => {
	acc[i] = color
	return acc
}, {})
const viridisFull = colormap({
	colormap: 'jet',
	nshades: 100,
	format: 'hex',
	alpha: 0.4
}).reduce((acc, color, i) => {
	acc[i] = color
	return acc
}, {})

const cool = colormap({
	colormap: 'cool',
	nshades: 20,
	format: 'hex',
	alpha: 0.5
}).reduce((acc, color, i) => {
	acc[i] = color
	return acc
}, {})
const coolFull = colormap({
	colormap: 'cool',
	nshades: 100,
	format: 'hex',
	alpha: 0.5
}).reduce((acc, color, i) => {
	acc[i] = color
	return acc
}, {})
const hot = colormap({
	colormap: 'hot',
	nshades: 20,
	format: 'hex',
	alpha: 0.5
}).reduce((acc, color, i) => {
	acc[i] = color
	return acc
}, {})
const hotFull = colormap({
	colormap: 'hot',
	nshades: 100,
	format: 'hex',
	alpha: 0.5
}).reduce((acc, color, i) => {
	acc[i] = color
	return acc
}, {})

/** @type {import('tailwindcss').Config} */
const config = {
	darkMode: ['class'],
	content: ['./src/**/*.{html,js,svelte,ts}'],
	safelist: [
		'dark',
		{
			pattern: /ring-([#e41a1c]|[#377eb8]|[#4daf4a])/
		},
		'data-[state=checked]:bg-jet-filter-0',
		'data-[state=checked]:bg-jet-filter-1',
		'data-[state=checked]:bg-jet-filter-2',
		'data-[state=checked]:bg-cool-filter-0',
		'data-[state=checked]:bg-cool-filter-1',
		'data-[state=checked]:bg-cool-filter-2',
		'data-[state=checked]:bg-hot-filter-0',
		'data-[state=checked]:bg-hot-filter-1',
		'data-[state=checked]:bg-hot-filter-2',
		{
			pattern: /bg-([#e41a1c]|[#377eb8]|[#4daf4a])/
		},
		{
			pattern: /bg-(jet|cool|hot)-.+/
		},
		{
			pattern: /(from|to|via)-(jet|cool|hot)-.+/
		},
		{
			pattern: /grid-cols-.+/
		}
	],
	theme: {
		container: {
			center: true,
			padding: '2rem',
			screens: {
				'2xl': '1400px'
			}
		},
		extend: {
			colors: {
				border: 'hsl(var(--border) / <alpha-value>)',
				input: 'hsl(var(--input) / <alpha-value>)',
				ring: 'hsl(var(--ring) / <alpha-value>)',
				background: 'hsl(var(--background) / <alpha-value>)',
				foreground: 'hsl(var(--foreground) / <alpha-value>)',
				primary: {
					DEFAULT: 'hsl(var(--primary) / <alpha-value>)',
					foreground: 'hsl(var(--primary-foreground) / <alpha-value>)'
				},
				secondary: {
					DEFAULT: 'hsl(var(--secondary) / <alpha-value>)',
					foreground: 'hsl(var(--secondary-foreground) / <alpha-value>)'
				},
				destructive: {
					DEFAULT: 'hsl(var(--destructive) / <alpha-value>)',
					foreground: 'hsl(var(--destructive-foreground) / <alpha-value>)'
				},
				muted: {
					DEFAULT: 'hsl(var(--muted) / <alpha-value>)',
					foreground: 'hsl(var(--muted-foreground) / <alpha-value>)'
				},
				accent: {
					DEFAULT: 'hsl(var(--accent) / <alpha-value>)',
					foreground: 'hsl(var(--accent-foreground) / <alpha-value>)'
				},
				popover: {
					DEFAULT: 'hsl(var(--popover) / <alpha-value>)',
					foreground: 'hsl(var(--popover-foreground) / <alpha-value>)'
				},
				card: {
					DEFAULT: 'hsl(var(--card) / <alpha-value>)',
					foreground: 'hsl(var(--card-foreground) / <alpha-value>)'
				},
				jet: {
					default: jet,
					filter: {
						0: jet[0],
						1: jet[10],
						2: jet[19]
					},
					value: viridisFull
				},
				cool: {
					default: cool,
					filter: {
						0: cool[0],
						1: cool[10],
						2: cool[19]
					},
					value: coolFull
				},
				hot: {
					default: hot,
					filter: {
						0: hot[0],
						1: hot[10],
						2: hot[19]
					},
					value: hotFull
				}
			},
			borderRadius: {
				lg: 'var(--radius)',
				md: 'calc(var(--radius) - 2px)',
				sm: 'calc(var(--radius) - 4px)'
			},
			fontFamily: {
				sans: [...fontFamily.sans]
			}
		}
	}
}

export default config
