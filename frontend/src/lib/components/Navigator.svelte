<script lang="ts">
	import { page } from '$app/stores'
	import { ROUTES } from '../../types'
	import { Button } from './ui/button'
	import { Label } from './ui/label'

	export let direction: 'horizontal' | 'vertical' = 'horizontal'
	export let drawer = false

	const directionStyle = {
		horizontal: 'flex-row space-x-2',
		vertical: 'flex-col space-y-2'
	}
	const routes = drawer ? ROUTES : ROUTES.slice(1)
</script>

<div class="flex {directionStyle[direction]}">
	{#each routes as route}
		<Button
			href={route.path}
			variant={drawer ? 'ghost' : 'outline'}
			class="h-fit {$page.route.id == route.id && 'bg-accent'}"
		>
			<div class="flex w-full cursor-pointer flex-col space-y-2 text-pretty">
				<div class="flex w-full cursor-pointer flex-row items-center space-x-2 text-pretty">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width="24"
						height="24"
						viewBox="0 0 24 24"
						class="ml-1 mt-0 cursor-pointer"
					>
						<path fill="black" d="M8.025 22L6.25 20.225L14.475 12L6.25 3.775L8.025 2l10 10z" />
					</svg>
					<Label class="mt-0 cursor-pointer text-lg">{route.title}</Label>
				</div>
				<Label class="text-muted-foreground max-w-80 cursor-pointer text-sm font-normal">
					{route.description}
				</Label>
			</div>
		</Button>
	{/each}
</div>
