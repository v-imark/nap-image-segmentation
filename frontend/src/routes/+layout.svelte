<script>
	import '../app.pcss'
	import * as Sheet from '$lib/components/ui/sheet'
	import { Button } from '$lib/components/ui/button'
	import { openDrawer } from '../stores'
	import Navigator from '$lib/components/Navigator.svelte'
	import Separator from '$lib/components/ui/separator/separator.svelte'
</script>

<Sheet.Root bind:open={$openDrawer}>
	<div class="h-screen">
		<Sheet.Trigger class="absolute bottom-1 right-1">Open</Sheet.Trigger>
		<slot />
	</div>
	<Sheet.Content side="left" class="space-y-2">
		<Sheet.Header>
			<Sheet.Title>Switch page</Sheet.Title>
			<Sheet.Description>
				This action cannot be undone. This will permanently delete your account and remove your data
				from our servers.
			</Sheet.Description>
		</Sheet.Header>
		<Separator />
		<Navigator direction="vertical" drawer />
	</Sheet.Content>
</Sheet.Root>
