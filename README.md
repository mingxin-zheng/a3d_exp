# a3d_exp

## Local
```
docker run -it --rm --ipc=host --gpus all --net host nvcr.io/nvidian/dlmed/monai-toolkit:2.0 bash -c "git clone https://github.com/mingxin-zheng/a3d_exp.git && cd a3d_exp && python main.py --num_node 2"
```

## NGC Base Command:

```
# single
ngc base-command job run 
	--name "ml-model.NOTPL_a3d_exp_1" 
	--priority NORMAL 
	--order 50 
	--preempt RUNONCE 
	--min-timeslice 2592000s 
	--total-runtime 2592000s 
	--ace nv-us-south-1 
	--instance dgxa100.80g.8.norm 
	--commandline "git clone https://github.com/mingxin-zheng/a3d_exp.git && cd a3d_exp && python main.py" 
	--result /results 
	--image "nvidian/dlmed/monai-toolkit:2.0" 
	--org nvidian 
	--team dlmed 
	--label _wl___computer_vision

# two
ngc base-command job run 
	--name "Job-nv-us-south-1-652915" 
	--priority NORMAL 
	--preempt RUNONCE 
	--min-timeslice 2592000s 
	--total-runtime 2592000s 
	--ace nv-us-south-1 
	--instance dgxa100.80g.8.norm 
	--commandline "git clone https://github.com/mingxin-zheng/a3d_exp.git && cd a3d_exp && python main.py --num_node 2" 
	--result /results 
	--array-type "PYTORCH" 
	--replicas "2" 
	--image "nvidian/dlmed/monai-toolkit:2.0" 
	--org nvidian 
	--team dlmed 
	--label _wl___computer_vision
```