#!/bin/bash

alias k="kubectl"
alias kx="kubectx"
alias kn="kubens"

alias kfails='kubectl get po -owide --all-namespaces | grep "0/" | tee /dev/tty | wc -l'

alias ki="kubectl-inspect "

alias ked="EDITOR=vim kubectl edit " 

alias kexec="kubectl exec -it"

alias klogs="kubectl logs -f"

alias kdd="kubectl delete"

alias kg="kubectl get"
alias kgi="kubectl get ing"
alias kgp="kubectl get pods"
alias kgs="kubectl get services"
alias kgd="kubectl get deploy"
alias kgh="kubectl get hpa"
alias kgss="kubectl get secrets"
alias kgep="kubectl get endpoints "

alias kd="kubectl describe"
alias kdp="kubectl describe pods $pod"

alias clsdb="export KUBECONFIG=~/k8s/sandbox/config"
alias cltools="export KUBECONFIG=~/k8s/tools/config"
alias clhmlinside="export KUBECONFIG=~/k8s/hml-inside/config"
alias clhmldmz="export KUBECONFIG=~/k8s/hml-dmz/config"
alias clprodinside="export KUBECONFIG=~/k8s/prod-inside/config"
alias clproddmz="export KUBECONFIG=~/k8s/prod-dmz/config"
