NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 \
torchrun --nproc_per_node 1 \
-m run-vehicle --indices_filename=global_indices-vehicle.json --batch_size=8