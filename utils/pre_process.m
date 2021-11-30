function out = pre_process(audio)
    audio = audio - mean(audio);
    audio = audio / max(abs(audio));
    out = audio;
end