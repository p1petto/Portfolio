import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.2


Window {
    minimumWidth: 360
    minimumHeight: 640
    visible: true
    Page{
        id:page
        anchors.fill:parent

        footer: ToolBar {
            height: 100
            Label {
                width: parent.width

                text: "Слайдер можно полистать с:"
                elide: Label.ElideRight
                horizontalAlignment: Qt.AlignHCenter
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
            }
        }


        Item{
            id: container
            width: parent.width/1.5
            height: parent.height/3
            anchors.centerIn: parent

            SwipeView {
                id: view

                currentIndex: 1
                anchors.fill: parent

                clip:true

                My_Page {
                    id: firstPage
                    backgroundColor: "red"
                }
                My_Page {
                    id: secondPage
                    backgroundColor: "yellow"
                }
                My_Page {
                    id: thirdPage
                    backgroundColor: "green"
                }
            }

            PageIndicator {
                id: indicator

                count: view.count
                currentIndex: view.currentIndex

                anchors.bottom: view.bottom
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

    }



}
