<script lang="ts">
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu'
	import { showFinal, showRemovedByIou, showRemovedByMinArea } from '../../stores'
	import { BG_COLORS } from '../../types'
	import { Button } from './ui/button'
	import { Checkbox } from './ui/checkbox'
	import { Label } from './ui/label'
</script>

<DropdownMenu.Root closeOnItemClick={false}>
	<DropdownMenu.Trigger asChild let:builder>
		<Button builders={[builder]} variant="outline" class="font-normal">Display Options</Button>
	</DropdownMenu.Trigger>
	<DropdownMenu.Content>
		<DropdownMenu.Group>
			<DropdownMenu.Label>Which masks to display</DropdownMenu.Label>
			<DropdownMenu.Item>
				<div class="flex items-center space-x-2">
					<Checkbox id="terms" bind:checked={$showRemovedByMinArea} />
					<Label
						for="terms"
						class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
					>
						Removed by min-area
					</Label>
					<div class="size-3 rounded {BG_COLORS[0]}" />
				</div>
			</DropdownMenu.Item>
			<DropdownMenu.Item>
				<div class="flex items-center space-x-2">
					<Checkbox id="terms" bind:checked={$showRemovedByIou} />
					<Label
						for="terms"
						class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
					>
						Removed by iou_threshold
					</Label>
					<div class="size-3 rounded {BG_COLORS[1]}" />
				</div>
			</DropdownMenu.Item>
			<DropdownMenu.Item>
				<div class="flex items-center space-x-2">
					<Checkbox id="terms" bind:checked={$showFinal} />
					<Label
						for="terms"
						class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
					>
						Final result
					</Label>
					<div class="size-3 rounded {BG_COLORS[2]}" />
				</div>
			</DropdownMenu.Item>
		</DropdownMenu.Group>
	</DropdownMenu.Content>
</DropdownMenu.Root>
