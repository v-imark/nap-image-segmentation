<script lang="ts">
	import * as Tooltip from '$lib/components/ui/tooltip'
	import { Label } from './ui/label'

	export let title: string = ''
	export let texts = ['Default']
</script>

<Tooltip.Root>
	<Tooltip.Trigger asChild let:builder>
		<slot {builder} />
	</Tooltip.Trigger>
	<Tooltip.Content side="left">
		<Label>{title}</Label>
		{#each texts as text}
			<p>{text}</p>
		{/each}
	</Tooltip.Content>
</Tooltip.Root>
