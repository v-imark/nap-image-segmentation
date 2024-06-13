<script lang="ts">
	import { page } from '$app/stores'
	import { cn } from '$lib/utils'
	import { crossfade } from 'svelte/transition'
	import { ROUTES } from '../../types'
	import { Button } from './ui/button'
	import { cubicInOut } from 'svelte/easing'

	const [send, receive] = crossfade({
		duration: 250,
		easing: cubicInOut
	})
</script>

<nav class="flex w-full flex-row space-x-2">
	{#each ROUTES as route}
		{@const isActive = $page.route.id === route.id}
		<Button
			href={route.path}
			variant="ghost"
			class={cn(
				!isActive && 'hover:bg-background',
				'hover:bg-muted-foreground relative justify-start rounded-b-none rounded-t-2xl py-2'
			)}
			data-sveltekit-noscroll
		>
			{#if isActive}
				<div
					class="bg-background absolute inset-0 rounded-t-2xl"
					in:send={{ key: 'active-sidebar-tab' }}
					out:receive={{ key: 'active-sidebar-tab' }}
				/>
			{/if}
			<div
				class={cn(
					'text-foreground relative text-lg uppercase',
					!isActive && 'text-primary-foreground'
				)}
			>
				{route.title}
			</div>
		</Button>
	{/each}
</nav>

<!-- <div class="flex {directionStyle[direction]}">
	{#each routes as route}
		<Button
			on:click={() => {
				goto(route.path)
			}}
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
</div> -->
