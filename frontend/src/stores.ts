import { writable } from 'svelte/store'

export const points_per_side = writable<number>(32)
export const points_per_batch = writable(64)
export const pred_iou_thresh = writable(0.88)
export const stability_score_thresh = writable(0.95)
export const crop_n_layers = writable(0)
export const crop_n_layers_downscale_factor = writable(1)
export const min_area = writable(0.01)
