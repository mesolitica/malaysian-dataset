NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 \
~/.local/bin/torchrun --nproc_per_node 4 \
-m run-tamil --batch_size=42