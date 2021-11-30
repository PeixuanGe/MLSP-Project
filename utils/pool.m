function [coeff_out,n_frames] = pool(coeff_in)
    N = size(coeff_in,1);
    length_pool = 1000:-100:100;
    for n = length_pool
        if N > n
            coeff_out = coeff_in(1:n,:);
            n_frames = n;
            break;
        end
    end
end