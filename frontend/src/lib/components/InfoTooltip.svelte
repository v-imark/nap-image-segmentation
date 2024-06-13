<script lang="ts">
	import { cn } from '$lib/utils'
	import type { ClassValue } from 'tailwind-variants'
	import { Label } from './ui/label'
	import * as Tooltip from './ui/tooltip'

	export let text = 'Example text'
	export let triggerStyle: ClassValue = undefined
</script>

<div class={cn('flex space-x-1', $$props.class)}>
	<slot />
	<Tooltip.Root>
		<Tooltip.Trigger>
			<div
				class={cn(
					'bg-muted hover:bg-accent flex size-5 items-center justify-center rounded-full',
					triggerStyle
				)}
			>
				<Label class="h-full w-full -indent-0.5 italic leading-normal">i</Label>
			</div>
		</Tooltip.Trigger>
		<Tooltip.Content>
			<p>{text}</p>
		</Tooltip.Content>
	</Tooltip.Root>
</div>
