@echo off
set basename=%0
set arg=%1


echo %arg%

if "%arg%"=="generate-keys" (
	
	call :sub_generate_keys
	
) else (
	if "%arg%"=="register-secrets" (
		call :register-secrets
	) else (
		call :sub_help
	)
)

pause
EXIT /B 0


:sub_help

    @ echo "Usage: %basename% <subcommand> \n"
    @ echo "Subcommands:"
    @ echo "    generate-keys      Generates private and public keys to be used to sign secrets"
    @ echo "    register-secrets   Signs the secrets and uploads them to Jenres API into the secrets repository"

EXIT /B 0


:sub_generate_keys 
@ echo "Running generate-keys command"

if not exist ".jenres" mkdir .jenres

openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4092 -outform pem -out .jenres/jenres_rsa_private.pem

openssl pkey -in .jenres/jenres_rsa_private.pem -pubout -out .jenres/jenres_rsa_public1.pem

copy .jenres\jenres_rsa_public1.pem .jenres\pub1.key

findstr /r ".jenres/jenres_rsa_public.pem" .gitignore > nul
if errorlevel 1 (
    @ echo .jenres/jenres_rsa_public.pem >> .gitignore
)

findstr /r ".jenres/jenres_rsa_private.pem" .gitignore > nul
if errorlevel 1 (
    @ echo .jenres/jenres_rsa_private.pem >> .gitignore
)

git add .gitignore .jenres/pub.key

@ echo "Keys generated and the public key has been added to Git index."
@ echo "Now you should review the changes, commit and push them." 
EXIT /B 0


:register-secrets
@ echo "Running register-secrets command"

set url="https://jenres-api.aws.res-it.com/secrets"
set private_key_path=".jenres/jenres_rsa_private.pem"

set /p openai_api_key="Enter OPENAI_API_KEY: "

@ echo "url: %url%"
@ echo "private_key_path: %private_key_path%"
@ echo "openai_api_key: %openai_api_key%"

set /p confirm="Are you sure you want to upload these secrets? (y/n) "

if %confirm%|findstr /r "[yY]" (
 @echo ""
 
 call jrepl "," ";" /inc -1 /f abc.java /o -
)

EXIT /B 0
