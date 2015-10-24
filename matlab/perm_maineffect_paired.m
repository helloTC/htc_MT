function [p_twoside, p_oneside, fig_pdist]=perm_maineffect_paired(sample1, sample2, stat_func, perm_times)

%perm_maineffect  Two sample general permutation test

[size1, size2, stat1, stat2] = two_sample_stat(sample1, sample2, stat_func);
tsize = size1 + size2;
tsample = [sample1; sample2];
effect_size = stat1 - stat2;
effect_size_perm = zeros(perm_times, 1);
for i = 1:perm_times
    index = randperm(tsize);
    s1 = tsample(index(1:size1), :);
    s2 = tsample(index((size1+1):tsize), :);
    effect_size_perm(i) = stat_func(s1)-stat_func(s2);
end

p_oneside = sum(effect_size_perm >= effect_size) / perm_times;
p_twoside = sum(abs(effect_size_perm) >= abs(effect_size)) / perm_times;

