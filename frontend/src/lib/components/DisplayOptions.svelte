<script lang="ts">
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu'
	import {
		colorMap,
		showFinal,
		showRemovedByIou,
		showRemovedByMinArea,
		strategy
	} from '../../stores'
	import { BG_COLORS, BORDER_COLORS } from '../../types'
	import InfoTooltip from './InfoTooltip.svelte'
	import { Button } from './ui/button'
	import { Checkbox } from './ui/checkbox'
	import { Label } from './ui/label'

	$: filterStrategy = $strategy == 'filter'
</script>

<div class="flex basis-1/2 flex-col space-y-1">
	<InfoTooltip
		text="Choose which masks should be displayed. Will have corresponding color if strategy=filter."
	>
		<Label class="text-lg">Masks to display</Label>
	</InfoTooltip>
	<div class="flex items-center space-x-2">
		<Checkbox
			bind:checked={$showRemovedByMinArea}
			class="flex size-5 items-center justify-center rounded-full {filterStrategy &&
				`data-[state=checked]:bg-${$colorMap}-filter-0`} peer border-2"
		/>
		<Label
			class="text-sm font-medium leading-none opacity-70 peer-data-[state=checked]:opacity-100"
		>
			Masks removed by min-area filter
		</Label>
	</div>
	<div class="flex items-center space-x-2">
		<Checkbox
			bind:checked={$showRemovedByIou}
			class="flex size-5 items-center justify-center rounded-full {filterStrategy &&
				`data-[state=checked]:bg-${$colorMap}-filter-1`} peer border-2"
		/>
		<Label
			class="text-sm font-medium leading-none opacity-70 peer-data-[state=checked]:opacity-100"
		>
			Masks removed by IoU filter
		</Label>
	</div>
	<div class="flex items-center space-x-2">
		<Checkbox
			bind:checked={$showFinal}
			class="flex size-5 items-center justify-center rounded-full {filterStrategy &&
				`data-[state=checked]:bg-${$colorMap}-filter-2`} border-2 {$colorMap == 'hot' &&
				'data-[state=checked]:text-black'} peer"
		/>
		<Label
			for="terms"
			class="text-sm font-medium leading-none opacity-70 peer-data-[state=checked]:opacity-100"
		>
			The final resulting masks
		</Label>
	</div>
</div>
