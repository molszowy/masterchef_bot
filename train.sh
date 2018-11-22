python3 -m rasa_core.train -c rasa_config.yml -d domain.yml -s stories.md -o models/restaurant --endpoints endpoints.yml
python3 -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project restaurant --verbose
python3 -m rasa_core_sdk.endpoint --actions actions