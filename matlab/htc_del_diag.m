function a = htc_del_diag(a_ori)
	a = a_ori - diag(diag(a_ori));
end
