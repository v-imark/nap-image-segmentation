<script>
	import '../app.pcss'
	import * as Sheet from '$lib/components/ui/sheet'
	import { openDrawer } from '../stores'
	import Navigator from '$lib/components/Navigator.svelte'
	import Separator from '$lib/components/ui/separator/separator.svelte'
</script>

<Sheet.Root bind:open={$openDrawer}>
	<div class="flex h-screen w-full flex-col">
		<div class="bg-primary w-full basis-auto px-3 pt-1">
			<Navigator />
		</div>
		<slot />
	</div>
	<Sheet.Content side="left" class="space-y-2">
		<Sheet.Header>
			<Sheet.Title>Switch page</Sheet.Title>
			<Sheet.Description></Sheet.Description>
		</Sheet.Header>
		<Separator />
		<Navigator />
	</Sheet.Content>
</Sheet.Root>
