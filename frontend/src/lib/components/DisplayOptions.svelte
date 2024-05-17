<script lang="ts">
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu'
	import { showFinal, showRemovedByIou, showRemovedByMinArea } from '../../stores'
	import { BG_COLORS, BORDER_COLORS } from '../../types'
	import { Button } from './ui/button'
	import { Checkbox } from './ui/checkbox'
	import { Label } from './ui/label'
</script>

<div class="flex flex-col space-y-1">
	<Label class="text-lg">Masks to display</Label>
	<div class="flex items-center space-x-2">
		<Checkbox
			id="minarea"
			bind:checked={$showRemovedByMinArea}
			class="flex size-5 items-center justify-center rounded-full data-[state=checked]:{BG_COLORS[0]} {BORDER_COLORS[0]} border-2"
		/>
		<Checkbox
			id="iou"
			bind:checked={$showRemovedByIou}
			class="flex size-5 items-center justify-center rounded-full data-[state=checked]:{BG_COLORS[1]} {BORDER_COLORS[1]} border-2"
		/>
		<Checkbox
			id="final"
			bind:checked={$showFinal}
			class="flex size-5 items-center justify-center rounded-full data-[state=checked]:{BG_COLORS[2]} {BORDER_COLORS[2]} border-2"
		/>
	</div>
</div>
