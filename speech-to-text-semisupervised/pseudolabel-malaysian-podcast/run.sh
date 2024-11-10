NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 \
torchrun --nproc_per_node 2 \
-m run --batch_size=2