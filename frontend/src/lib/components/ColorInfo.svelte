<script lang="ts">
	import { BG_COLORS } from '../../types'
	import { Label } from './ui/label'
</script>

<div class="flex flex-col space-y-1">
	<Label class="text-lg">Color Information</Label>
	<div class="flex items-center space-x-2">
		<div class="size-5 rounded-full {BG_COLORS[0]}" />
		<Label
			for="terms"
			class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
		>
			Masks removed by min-area filter
		</Label>
	</div>
	<div class="flex items-center space-x-2">
		<div class="size-5 rounded-full {BG_COLORS[1]}" />
		<Label
			for="terms"
			class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
		>
			Masks removed by IoU filter
		</Label>
	</div>
	<div class="flex items-center space-x-2">
		<div class="size-5 rounded-full {BG_COLORS[2]}" />
		<Label
			for="terms"
			class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
		>
			The final resulting masks
		</Label>
	</div>
</div>
