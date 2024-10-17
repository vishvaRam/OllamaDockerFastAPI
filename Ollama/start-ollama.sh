
./bin/ollama serve &

pid=$!

sleep 5


echo "Pulling qwen2.5:0.5b model"
ollama pull qwen2.5:0.5b


wait $pid