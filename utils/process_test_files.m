filedir = './wav/';
mkdir testfiles;

f = fopen('./iden_split.txt','r');
index_file = fopen('./test_index.txt', 'wt' );
line = fgetl(f);
counter = 0;
while ischar(line)
    strs = split(line, ' ');
    class = str2double(strs{1});
    if class == 3
        counter = counter+1;
        [audio,fs] = audioread([filedir strs{2}]);
        
        audio = pre_process(audio);
        coeff = mfcc(audio,fs,'WindowLength',round(fs*0.05),'OverlapLength',round(fs*0.025),'NumCoeffs',40);
        writematrix(coeff,['testfiles/' int2str(counter) '.csv']);
        str2 = split(strs{2}, '/');
        id = strrep(str2{1},'id','');
        fprintf(index_file, [id '\n']);
        %disp(strs{2});
    end
    line = fgetl(f);
end
fclose(f);
fclose(index_file);