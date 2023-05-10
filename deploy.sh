set -e
python parse_variables.py
source .conf.sh
gcloud builds submit \
	--substitutions=_LOCATION=$_LOCATION,_PROJECT_ID=$_PROJECT_ID,_TAG=$_TAG,_IMAGE=$_IMAGE,_REPO=$_REPO,_SERVICE_NAME=$_SERVICE_NAME

