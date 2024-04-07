<script lang="ts">
	import Chart from 'chart.js/auto'
	import { PARAM_IDS } from '../../api'
	import { all_data, run, selected_name } from '../../stores'
	import type { Metadata } from '../../types'

	const formatData = (data: Metadata) =>
		PARAM_IDS($run).map((id) => {
			const masks = data[id] ? data[id].masks : []
			return {
				label: id,
				data: masks.map((mask) => {
					return { x: mask.predicted_iou, y: mask.stability_score, r: 3 + mask.area / 5000 }
				})
			}
		})
	const renderChart = (ctx: HTMLCanvasElement, data: Metadata) => {
		const chart = new Chart(ctx, {
			type: 'bubble',
			data: {
				labels: PARAM_IDS($run),
				datasets: formatData(data)
			},
			options: {
				scales: {
					y: {
						title: {
							display: true,
							text: 'stability_score'
						}
					},
					x: {
						title: {
							display: true,
							text: 'predicted_iou'
						}
					}
				},
				plugins: {
					title: {
						display: true,
						text: `All masks produced from ${$selected_name}`
					},
					subtitle: {
						display: true,
						text: 'Radius of points = area of mask'
					}
				}
			}
		})
		return {
			update() {
				chart.update()
			},
			destroy() {
				chart.destroy()
			}
		}
	}
</script>

{#await $all_data then data}
	<div class="chart-container h-{192} w-{192}">
		<canvas use:renderChart={data}></canvas>
	</div>
{/await}
