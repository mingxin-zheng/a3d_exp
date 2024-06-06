# a3d_exp

## Local
```
docker run -it --rm --ipc=host --gpus all --net host nvcr.io/nvidian/dlmed/monai-toolkit:2.0 bash -c "git clone https://github.com/mingxin-zheng/a3d_exp.git && cd a3d_exp && python main.py --num_node 2"
```

## NGC Base Command:

```
# single
ngc base-command job run --name "ml-model.NOTPL_a3d_exp_1" \
	--image "nvidian/dlmed/monai-toolkit:2.0" \
	--preempt RUNONCE \
	--ace nv-us-south-1 \
	--instance dgxa100.80g.8.norm \
	--result /results \
	--label _wl___computer_vision \
	--commandline "git clone https://github.com/mingxin-zheng/a3d_exp.git && cd a3d_exp && python main.py"

# 2 nodes
ngc base-command job run --name "ml-model.NOTPL_a3d_exp_3" \
	--image "nvidian/dlmed/monai_dev:20230913" \
	--preempt RUNONCE \
	--total-runtime 2592000s
	--ace nv-us-west-2 \
	--instance dgx1v.32g.8.norm \
	--result /results \
	--array-type "PYTORCH" \
	--replicas "2" \
	--label _wl___computer_vision \
	--commandline "\
git clone https://github.com/mingxin-zheng/a3d_exp.git && \
cd a3d_exp && \
python main.py --num_node 2
" # donotmiss

# interactive
ngc base-command job run --name "ml-model.NOTPL_interactive" \
	--image "nvidian/dlmed/monai_dev:20230913" \
	--preempt RUNONCE \
	--total-runtime 18000s \
	--ace nv-us-west-2 \
	--instance dgx1v.32g.8.norm \
	--result /results \
	--array-type "PYTORCH" \
	--replicas "2" \
	--label _wl___computer_vision \
	--commandline "\
git clone https://github.com/mingxin-zheng/a3d_exp.git && \
cd a3d_exp && \
sleep 5h
" # donotmiss

# debug
ngc base-command job run --name "ml-model.NOTPL_debug" \
	--image "nvidian/dlmed/monai_dev:20230913" \
	--preempt RUNONCE \
	--ace nv-us-west-2 \
	--instance dgx1v.32g.8.norm \
	--result /results \
	--array-type "PYTORCH" \
	--replicas "2" \
	--label _wl___computer_vision \
	--commandline "
git clone https://github.com/mingxin-zheng/a3d_exp.git && \
cd a3d_exp && \
python debug.py
" # donotmiss
```

`export NGC_MASTER_ADDR=launcher-svc-\${NGC_JOB_ID}`
