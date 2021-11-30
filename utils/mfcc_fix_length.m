clear all;

filedir = './wav/';
mkdir coeffs;
for n = 1:1251 %1251
    if n<10
        id_num = [filedir,'id1000', int2str(n),'/'];
        coeff_dir_outer = ['id1000', int2str(n)];
        mkdir('coeffs',coeff_dir_outer);
    elseif n<100
        id_num = [filedir,'id100', int2str(n),'/'];
        coeff_dir_outer = ['id100', int2str(n)];
        mkdir('coeffs',coeff_dir_outer);
    elseif n<1000
        id_num = [filedir,'id10', int2str(n),'/'];
        coeff_dir_outer = ['id10', int2str(n)];
        mkdir('coeffs',coeff_dir_outer);
    else
        id_num = [filedir,'id1', int2str(n),'/'];
        coeff_dir_outer = ['id1', int2str(n)];
        mkdir('coeffs',coeff_dir_outer);
    end
    
    sub_dirs = dir(id_num);
    for m = 1:length(sub_dirs)-2
        file_dir = [id_num,sub_dirs(m+2).name,'/'];
        
        mkdir(['coeffs/',coeff_dir_outer],sub_dirs(m+2).name);
        final_dir = ['coeffs/',coeff_dir_outer,'/',sub_dirs(m+2).name,'/'];
        files = dir(file_dir);
        parfor l = 1:length(files)-2
           [audio,fs] = audioread([file_dir,files(l+2).name]);
           audio = pre_process(audio);
%%%%%%%%            audio = noise_padding(audio,2318721); %%%%%%% noise padding
%%%%%%%%           audio = zero_padding(audio,2318721); %%%%%%%%% zero padding
           
           coeff = mfcc(audio,fs,'WindowLength',round(fs*0.05),'OverlapLength',round(fs*0.025),'NumCoeffs',40); %14 coefficients for each window  
           
            coeff = coeff(1:157,:); %%%%%%%%%% truncate mfcc

           if l < 10
               writematrix(coeff,[final_dir,'0000',int2str(l),'.csv']);
           elseif l < 100
               writematrix(coeff,[final_dir,'000',int2str(l),'.csv']);
           elseif l < 1000
               writematrix(coeff,[final_dir,'00',int2str(l),'.csv']);
           else
               writematrix(coeff,[final_dir,'0',int2str(l),'.csv']);
           end
        end
    end
end